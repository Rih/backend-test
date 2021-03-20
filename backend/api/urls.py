from django.urls import include, path
from account.views import user_view
from ejercicio_2.views import company_view, company_faker_view
from rest_framework.urlpatterns import format_suffix_patterns


app_name = 'api'
urlpatterns = [
    path(
        'user/<int:pk>/',
        user_view,
        name='users',
    ),
    path(
        'companies/',
        company_view,
        name='companies',
    ),
    path(
        'company/<int:pk>/',
        company_view,
        name='company',
    ),
    path(
        'faker/create-companies/',
        company_faker_view,
        name='company_faker',
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
