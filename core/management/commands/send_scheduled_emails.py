"""core.management.commands.send_scheduled_emails"""
from django.core.mail import EmailMessage, BadHeaderError
from django.core.management.base import BaseCommand

from core.models import ScheduledEmail


def get_email_list(emails_str):
    """
    Returns the comma separated email string as a list
    @return:
    """
    return [email.strip() for email in emails_str.split(',')]


class Command(BaseCommand):
    """
    The command class to send out emails queued in ScheduledEmails
    """
    help = 'Sends out emails queued in ScheduledEmails'

    def handle(self, *args, **options):
        emails = ScheduledEmail.objects.filter(
            status__in=[
                ScheduledEmail.SCHEDULED_EMAIL_STATUS_FAILED,
                ScheduledEmail.SCHEDULED_EMAIL_STATUS_PENDING
            ]
        )
        email: ScheduledEmail
        for email in emails:
            email_to_send = EmailMessage(
                email.subject,
                email.body,
                email.sender_address,
                get_email_list(email.to),
                get_email_list(email.cc),
            )
            try:
                email_to_send.send(fail_silently=False)
                email.status = ScheduledEmail.SCHEDULED_EMAIL_STATUS_SENT
                self.stdout.write(self.style.SUCCESS('Successfully sent the email.'))
            except BadHeaderError:
                email.status = ScheduledEmail.SCHEDULED_EMAIL_STATUS_FAILED
                self.stdout.write(self.style.ERROR('Invalid header found.'))
            except ConnectionRefusedError:
                email.status = ScheduledEmail.SCHEDULED_EMAIL_STATUS_FAILED
                self.stdout.write(self.style.ERROR('Connection refused'))
            email.save()
