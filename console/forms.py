"""console.forms"""
# pylint: disable=imported-auth-user
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator, validate_email
from django.forms import Form


class MultiEmailInviteForm(Form):
    """
    Form for creating a new user
    """

    email_str_max_length = 3000
    max_emails = 100
    help_text = 'Required. {max_len} characters or fewer. Maximum {max_emails} emails'

    emails = forms.CharField(
        widget=forms.Textarea,
        label='Emails',
        required=True,
        max_length=email_str_max_length,
        validators=[MaxLengthValidator(email_str_max_length)],
        help_text=help_text.format(
            max_len=email_str_max_length,
            max_emails=max_emails
        ),
    )

    def clean_emails(self):
        """
        Non empty list of comma separated emails.
        Only a maximum of 100 emails per one go
        Only valid email addresses (syntactically)
        """
        emails_str = self.cleaned_data['emails']

        if not emails_str or not emails_str.strip():
            raise ValidationError('Please add some email addresses')

        emails = self.get_email_list()

        if len(emails) > self.max_emails:
            raise ValidationError(
                'Cannot add more than {max_emails} emails'.format(
                    max_emails=self.max_emails
                )
            )

        invalid_emails = []
        for email in emails:
            try:
                validate_email(email)
            except forms.ValidationError:
                invalid_emails.append(email)

        if len(invalid_emails) > 0:
            invalid_email_str = ','.join(invalid_emails)
            raise ValidationError(
                'These emails are invalid: {emails}'.format(
                    emails=invalid_email_str
                )
            )
        return emails_str

    def get_email_list(self):
        """
        Returns the comma separated email string as a list
        @return:
        """
        emails_str = self.cleaned_data['emails']
        return [email.strip() for email in emails_str.split(',')]
