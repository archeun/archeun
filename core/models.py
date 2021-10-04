"""core.models"""
# pylint: disable=imported-auth-user
from django.contrib.auth.models import User
from django.db import models


class Employee(models.Model):
    """
    Employee model by extending the User model
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{firstname} {lastname} ({email})".format(
            firstname=self.user.first_name,
            lastname=self.user.last_name,
            email=self.user.email
        )

    class Meta:
        db_table = 'arch_core_employee'


class ScheduledEmail(models.Model):
    """
    Model to save the emails that are scheduled to be sent
    """

    SCHEDULED_EMAIL_STATUS_PENDING = 'PENDING'
    SCHEDULED_EMAIL_STATUS_SENT = 'SENT'
    SCHEDULED_EMAIL_STATUS_FAILED = 'FAILED'

    SCHEDULED_EMAIL_STATUSES = [
        (SCHEDULED_EMAIL_STATUS_PENDING, 'Pending'),
        (SCHEDULED_EMAIL_STATUS_SENT, 'Sent'),
        (SCHEDULED_EMAIL_STATUS_FAILED, 'Failed'),
    ]

    to_emails = models.TextField()
    cc_emails = models.TextField(blank=True, null=True)
    sender_address = models.CharField(max_length=255)
    sender_name = models.CharField(max_length=255)
    subject = models.CharField(max_length=1000)
    body = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=SCHEDULED_EMAIL_STATUSES,
        default='PENDING',
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'arch_core_scheduled_email'
