from django.contrib.auth.forms import UserCreationForm as BaseCreateAccountForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError


class CreateAccountForm(BaseCreateAccountForm):
    first_name = forms.CharField(
        label='First Name', min_length=1, max_length=200)
    last_name = forms.CharField(
        label='Last Name', min_length=1, max_length=200)
    email = forms.EmailField(label='Email')

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError("Email already exists")
        return email

    def clean_first_name(self):
        return self.cleaned_data['first_name']

    def clean_last_name(self):
        return self.cleaned_data['last_name']

    class Meta:
        model = User
        fields = ["username", "password1", "password2",
                  "first_name", "last_name", "email"]
