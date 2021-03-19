import factory
from factory import SubFactory
from django.contrib.auth import get_user_model
User = get_user_model()


class UserAccountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = 'John'
    last_name = 'Doe'
    username = 'user'
    email = 'email@admin.cl'


class RoleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Role
    name = 'mi_role'
