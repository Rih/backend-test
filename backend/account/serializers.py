from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['pk'] = user.pk
        token['email'] = user.email
        return token

    def validate(self, attrs, **kwargs):
        # The default result (access/refresh tokens)
        attrs['email'] = attrs['username']
        data = super(MyTokenObtainPairSerializer, self).validate(attrs)
        # Custom data you want to include
        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# Scafold serializer User
class UserModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
