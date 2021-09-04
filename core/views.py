from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.views.generic.edit import FormView
from core.forms import CreateAccountForm


class BaseUserView(LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL


class UserProfileView(BaseUserView):
    def get(self, request):
        return render(request, 'user/profile.html')


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
