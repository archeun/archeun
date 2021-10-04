"""core.services.scheduled_email_service"""
from django.conf import settings
from core.models import ScheduledEmail


def schedule(
        to_emails,
        subject,
        body,
        cc_emails='',
        sender_name=settings.ARCHEUN['core']['email']['sender_name']):
    """
    Populate and save the ScheduledEmail in the database
    @param to_emails:
    @param subject:
    @param body:
    @param cc_emails:
    @param sender_name:
    @return:
    """
    scheduled_email = ScheduledEmail()
    scheduled_email.to = to_emails
    scheduled_email.cc = cc_emails
    scheduled_email.sender_address = settings.ARCHEUN['core']['email']['sender_address']
    scheduled_email.sender_name = sender_name
    scheduled_email.subject = subject
    scheduled_email.body = body
    scheduled_email.save()
