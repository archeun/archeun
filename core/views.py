from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.conf import settings
from core.forms import CreateAccountForm


class BaseUserView(LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL


class UserProfileView(BaseUserView):
    def get(self, request):
        return render(request, 'user/profile.html')


class CreateAccountView(View):
    def get(self, request):
        return render(request, 'auth/create_account.html', {'form': CreateAccountForm()})

    '''
    TODO: Refactor this function to handle the error messages properly
    TODO: Upon re direction preserve filled values
    '''
    def post(self, request):
        form = CreateAccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_account_success')
        else:
            form_errors = dict(form.errors)
            errors = {
                "Username": form_errors.get("username", False),
                "Password Confirmation": form_errors.get("password", False),
                "Password": form_errors.get("password2", False),
                "Email": form_errors.get("email", False),
                "First Name": form_errors.get("first_name", False),
                "Last Name": form_errors.get("last_name", False),
            }
            for fieldname in errors:
                if errors[fieldname]:
                    errormessage = '<ul><li>' + fieldname + '</li><ul>'
                    fielderrors = errors[fieldname]
                    for fielderror in fielderrors:
                        errormessage = errormessage + '<li>' + fielderror + '</li>'

                    errormessage = errormessage + '</ul></ul>'
                    messages.add_message(
                        request,
                        messages.ERROR,
                        errormessage
                    )
            return redirect('create_account')


class CreateAccountSuccessView(View):
    def get(self, request):
        return render(request, 'auth/create_account_success.html')
