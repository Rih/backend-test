import factory
import datetime
import random
from django.contrib.auth import get_user_model
User = get_user_model()


class UserAccountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = 'John'
    last_name = 'Doe'
    username = 'user'
    email = 'email@admin.cl'
    date_joined = factory.LazyFunction(datetime.datetime.now)

