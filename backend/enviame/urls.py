"""ifn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from account.views import CustomTokenObtainPairView, PermissionsView
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='API', url='/swagger')

admin.autodiscover()

urlpatterns = [
    url(r'^swagger/$', schema_view),
    path('grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', admin.site.urls),
    path('api/v1/', include('visor.urls', namespace='api')),
    path('api-account/v1/', include('account.urls', namespace='api_account')),
    path('api-visor/v1/', include('visor.urls', namespace='api_visor')),
    path('api-xstock/v1/', include('xstock.urls', namespace='api_xstock')),
    path('api-extractor/v1/', include('extractor.urls', namespace='api_extractor')),
    path('api/v1/token/permissions/', PermissionsView.as_view(), name='token_permissions0'),
    path('api-visor/v1/token/permissions/', PermissionsView.as_view(), name='token_permissions1'),
    path('api-xstock/v1/token/permissions/', PermissionsView.as_view(), name='token_permissions2'),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
