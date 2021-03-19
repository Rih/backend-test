from django.shortcuts import render
from account.serializers import MyTokenObtainPairSerializer, UserSerializer, \
    RoleSerializer, GroupSerializer, UserModelSerializer, \
    UserPasswordModelSerializer, UserCreationModelSerializer, \
    UserValidationModelSerializer, UserResetPasswordModelSerializer
from account.models import Role
from account.bl import user_profile
from django.contrib.auth.hashers import check_password
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from rest_framework import status, permissions
from rest_framework import generics
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework.views import APIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from account.data import RECAPTCHA_MIN_SCORE
from account.bl import recaptcha, role
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.conf import settings

# Create your views here.


# returns { refresh, access, recaptcha }
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        response = recaptcha.validate_captcha(request.data.get('recaptchaToken'))
        tokens = MyTokenObtainPairSerializer(request.data).validate(
            request.data,
            recaptcha_result=response
        )
        return Response(tokens, status=status.HTTP_200_OK)


class UserCreationView(APIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = UserCreationModelSerializer

    def get(self, request, *args, **kwargs):
        user = user_profile.existing_user(email='rodrigo@sistematiza.cl')
        user.send_recovery()
        return render(request, 'account/templates/recovery.html', {'data': '234234'})

    # tested at tests.test_api_account_post_creation
    def post(self, request, *args, **kwargs):
        response = recaptcha.validate_captcha(request.data.get('recaptchaToken'))
        user_email = user_profile.existing_user(email=request.data['email'])
        data = user_profile.get_data('creation', request.data)
        serializer = UserCreationModelSerializer(user_email, data=data)
        if serializer.is_valid():
            serializer.save()
            user_created = user_profile.existing_user(
                email=request.data['email']
            )
            user_created.send_creation()
            result = request.data.copy()
            result['username'] = request.data['email']
            tokens = MyTokenObtainPairSerializer(result).validate(
                result,
                recaptcha_result=response
            )
            result.update(tokens)
            del result['password']
            return Response(result, status=status.HTTP_201_CREATED)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class UserModelView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserModelSerializer

    def get_object(self):
        try:
            return User.objects.get(pk=self.request.user.pk)
        except User.DoesNotExist:
            raise Http404

    # tested at tests.test_api_account_put_profile
    # and test_api_account_put_validate
    def put(self, request, *args, **kwargs):
        user = self.get_object()
        type_put = request.GET.get('type')
        data = user_profile.get_data(type_put, request.data)
        if type_put == 'validate':  # TODO: maybe move to POST
            received = request.data.copy()
            logged = User.objects.get(pk=request.user.pk)
            return Response({
                'result': check_password(received['password'], logged.password)
            })
        serialize = user_profile.get_serializer(type_put)
        serializer = serialize(user, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            result = serializer.data.copy()
            if type_put == 'password':
                del result['password']
            return Response(result)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        user = self.get_object(kwargs.get('pk')) if kwargs.get('pk') else self.get_object(request.user.id)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class PermissionsView(generics.ListAPIView):
    serializer_class = RoleSerializer
    permission_classes = [IsAuthenticated]
    # permission_classes = []

    def get(self, request, *args, **kwargs):
        if request.user:
            role = Role.objects.filter(user=request.user.id)
            serializer_role = RoleSerializer(role, many=True)
            return Response(serializer_role.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_403_FORBIDDEN)


class RecoveryView(APIView):
    serializer_class = UserValidationModelSerializer
    permission_classes = []
    authentication_classes = []

    def get_object(self, pk, recovery):
        try:
            return User.objects.get(pk=pk, token_recovery=recovery)
        except User.DoesNotExist:
            raise Http404

    # tested at tests.test_api_account_post_recovery
    def post(self, request, *args, **kwargs): # send email, change attribute status
        user = user_profile.existing_user(email=request.data.get('email'))
        response = recaptcha.validate_captcha(
            request.data.get('recaptchaToken')
        )
        if not response['success'] or response['score'] < RECAPTCHA_MIN_SCORE:
            return Response(
                {'invalid': 'recaptcha'},
                status=status.HTTP_400_BAD_REQUEST
            )
        if user:
            user.send_recovery(origin=request.data.get('origin'))
            serializer = UserValidationModelSerializer(user, data={
                'recovery_request': True,
            }, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    # tested at tests.test_api_account_put_recovery
    def put(self, request, *args, **kwargs):  # new password
        user = self.get_object(kwargs.get('pk'), kwargs.get('token'))
        response = recaptcha.validate_captcha(
            request.data.get('recaptchaToken')
        )
        if not response['success'] or response['score'] < RECAPTCHA_MIN_SCORE:
            return Response(
                {'invalid': 'recaptcha'},
                status=status.HTTP_400_BAD_REQUEST
            )
        user.refresh_recovery_token()
        data = request.data.copy()  # contains raw password
        user_data = user_profile.get_data('recovery', data)
        user_data['recovery_request'] = False
        serializer = UserResetPasswordModelSerializer(
            user,
            data=user_data,
            partial=True
        )
        if serializer.is_valid() and response['success']:
            serializer.save()
            data['username'] = user.email
            del data['password']
            return Response(data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class ValidateEmailView(APIView):
    serializer_class = UserSerializer
    permission_classes = []

    def get_object(self, pk, token):
        try:
            return User.objects.get(pk=pk, token_email=token)
        except User.DoesNotExist:
            return None

    # tested at tests.test_api_account_validate_email_get
    def get(self, request, *args, **kwargs):  # check stoken
        token = kwargs.get('token')
        # uid = force_text(urlsafe_base64_decode(kwargs.get('uidb64')))
        user = self.get_object(kwargs.get('pk'), token)
        if user:
            user.refresh_email_token()
            serializer = UserSerializer(user, data={
                'email_validated': True,
            }, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(
                    serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST
                )
        return Response({'url': 'invalid'}, status=status.HTTP_403_FORBIDDEN)
