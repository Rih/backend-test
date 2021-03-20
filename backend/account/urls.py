from django.urls import include, path
from account.views import user_view, company_view
from rest_framework.urlpatterns import format_suffix_patterns


app_name = 'account'
urlpatterns = [
    # user
    path(
        'api-auth/',
        include('rest_framework.urls', namespace='rest_framework'),
    ),
    #
]

urlpatterns = format_suffix_patterns(urlpatterns)
