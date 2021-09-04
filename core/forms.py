from django.contrib.auth.forms import UserCreationForm as BaseCreateAccountForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator


class CreateAccountForm(BaseCreateAccountForm):
    first_name = forms.CharField(
        label='First Name',
        min_length=1,
        max_length=150,
        validators=[MaxLengthValidator(150)],
        help_text='Required. 150 characters or fewer',
    )
    last_name = forms.CharField(
        label='Last Name',
        min_length=1,
        max_length=150,
        validators=[MaxLengthValidator(150)],
        help_text='Required. 150 characters or fewer',
    )
    email = forms.EmailField(
        label='Email',
        help_text='Required. A valid email address in the user@example.com format',
    )

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError("Email already exists")
        return email

    class Meta:
        model = User
        fields = ["username", "password1", "password2", "first_name", "last_name", "email"]
