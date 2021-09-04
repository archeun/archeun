from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.views.generic.edit import FormView
from django.contrib.auth import views as auth_views
from core.forms import CreateAccountForm


class BaseUserView(LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL


class UserProfileView(BaseUserView):
    def get(self, request):
        return render(request, 'user/profile.html')


class LoginView(auth_views.LoginView):
    template_name = 'auth/login.html'


class LogoutView(auth_views.LogoutView):
    template_name = 'auth/logout.html'


class CreateAccountView(FormView):
    template_name = 'auth/create_account.html'
    form_class = CreateAccountForm
    success_url = '/core/auth/create-account-success/'

    def form_valid(self, form):
        form.save()
        return super(CreateAccountView, self).form_valid(form)


class CreateAccountSuccessView(View):
    def get(self, request):
        return render(request, 'auth/create_account_success.html')


class PasswordResetView(auth_views.PasswordResetView):
    template_name = 'auth/password_reset_form.html'


class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'auth/password_reset_done.html'
