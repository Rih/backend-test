from django.urls import include, path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns


app_name = 'account'
urlpatterns = [
    # user
    path(
        'api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
    ),
    #
    path(
        'user/<int:pk>',
        UserDetail.as_view(),
        name='users'
    ),
    path(
        'account/',
        UserModelView.as_view(),
        name='account_profile'
    ),
    path(
        'account/new',
        UserCreationView.as_view(),
        name='account_creation'
    ),
    path(
        'account/recovery-request',
        RecoveryView.as_view(),
        name='account_recovery_request'
    ),
    path(
        'account/recovery/<int:pk>/<str:token>',
        RecoveryView.as_view(),
        name='account_recovery'
    ),
    path(
        'account/validation/<int:pk>/<str:token>',
        ValidateEmailView.as_view(),
        name='account_validation'
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
