from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from core.forms import CreateAccountForm


class BaseUserView(LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL


class UserProfileView(BaseUserView):
    def get(self, request):
        return render(request, 'user/profile.html')


class CreateAccountView(View):
    def get(self, request):
        return render(
            request,
            'auth/create_account.html',
            {'form': CreateAccountForm(), 'form_errors': request.session.pop('form_errors', {})}
        )

    '''
    TODO: Upon re direction preserve filled values
    '''

    def post(self, request):
        form = CreateAccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_account_success')
        else:
            request.session['form_errors'] = form.errors
            return redirect('create_account')


class CreateAccountSuccessView(View):
    def get(self, request):
        return render(request, 'auth/create_account_success.html')
