from django.shortcuts import render
from account.serializers import (
    MyTokenObtainPairSerializer,
    UserModelSerializer,
)
from rest_framework.response import Response
from rest_framework.decorators import action
from django.http import Http404
from rest_framework import status
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework.views import APIView
from django.conf import settings

# Create your views here.


class UserView(APIView):
    serializer_class = UserModelSerializer
    queryset = User.objects.all()

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        user = self.get_object(kwargs.get('pk'))
        serializer = UserModelSerializer(user)
        return Response(serializer.data)


user_view = UserView.as_view()
