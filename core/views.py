"""core.views module"""
from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.views.generic.edit import FormView
from django.contrib.auth import views as auth_views
from core.forms import CreateAccountForm


class BaseUserView(LoginRequiredMixin, View):
    """
    Base view to enable login required mixin for user related screens
    """
    login_url = settings.LOGIN_URL


class UserProfileView(BaseUserView):
    """
    User profile
    """

    def get(self, request):
        """
        Render the profile.html
        """
        return render(request, 'user/profile.html')


class LoginView(auth_views.LoginView):
    """
    Login
    """
    template_name = 'auth/login.html'


class LogoutView(auth_views.LogoutView):
    """
    Logout
    """
    template_name = 'auth/logout.html'


class CreateAccountView(FormView):
    """
    Create user account
    """
    template_name = 'auth/create_account.html'
    form_class = CreateAccountForm
    success_url = '/core/auth/create-account-success/'

    def form_valid(self, form):
        """
        This function is called if the user creation form is valid
        """
        form.save()
        return super().form_valid(form)


class CreateAccountSuccessView(View):
    """
    Redirected view upon successful account creation
    """

    def get(self, request):
        """
        Render the create_account_success.html
        """
        return render(request, 'auth/create_account_success.html')


class PasswordResetView(auth_views.PasswordResetView):
    """
    Password reset form to enter email address
    """
    template_name = 'auth/password_reset_form.html'


class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    """
    Password reset form submitted
    """
    template_name = 'auth/password_reset_done.html'


class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    """
    Password reset link will redirect to this view to change the actual password
    """
    template_name = 'auth/password_reset_confirm.html'


class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    """
    After successfully changing the password this view will be executed
    """
    template_name = 'auth/password_reset_complete.html'
