from django.contrib import admin
from django.urls import include, path, re_path

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('openid/', include('oidc_provider.urls', namespace='oidc_provider')),
]
