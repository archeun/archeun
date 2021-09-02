from django.contrib.auth import views as auth_views
from django.urls import include, path
from core.views import UserProfileView, CreateAccountView, CreateAccountSuccessView

urlpatterns = [
    path('openid/',
         include('oidc_provider.urls', namespace='oidc_provider')),

    path('auth/login/',
         auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),

    path('auth/logout/',
         auth_views.LogoutView.as_view(template_name='auth/logout.html'), name='logout'),

    path('auth/password_reset/',
         auth_views.PasswordResetView.as_view(), name='password_reset'),

    path('auth/create-account/',
         CreateAccountView.as_view(), name='create_account'),

    path('auth/create-account-success/',
         CreateAccountSuccessView.as_view(), name='create_account_success'),

    path('user/profile/',
         UserProfileView.as_view(), name='user_profile'),
]
