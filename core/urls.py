"""core.urls"""
from django.urls import include, path
from core import views as arch_core_views

urlpatterns = [
    path('openid/',
         include('oidc_provider.urls', namespace='oidc_provider')),

    path('auth/login/',
         arch_core_views.LoginView.as_view(template_name='auth/login.html'), name='login'),

    path('auth/logout/',
         arch_core_views.LogoutView.as_view(template_name='auth/logout.html'), name='logout'),

    # Form view for entering the email address to receive password reset link
    path('auth/password-reset/',
         arch_core_views.PasswordResetView.as_view(), name='password_reset'),

    # Once submitted the password_reset form, user will be redirected to this screen
    path('auth/password-reset-done/',
         arch_core_views.PasswordResetDoneView.as_view(), name='password_reset_done'),

    # Once clicked on the password reset link in the email user will be redirected to this screen
    # to change the password
    path('auth/password-reset-confirm/<uidb64>/<token>/',
         arch_core_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    # Once the change password form is submitted, user is redirected to this screen
    path('auth/password-reset-complete/',
         arch_core_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('auth/create-account/',
         arch_core_views.CreateAccountView.as_view(), name='create_account'),

    path('auth/create-account-success/',
         arch_core_views.CreateAccountSuccessView.as_view(), name='create_account_success'),

    path('user/profile/',
         arch_core_views.UserProfileView.as_view(), name='user_profile'),
]
