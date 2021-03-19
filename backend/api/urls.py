from django.urls import include, path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns


app_name = 'api'
urlpatterns = [
    # user
]

urlpatterns = format_suffix_patterns(urlpatterns)
