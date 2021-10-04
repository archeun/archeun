"""core.admin"""
from django.contrib import admin

from core.models import Employee, ScheduledEmail

admin.site.register(Employee)
admin.site.register(ScheduledEmail)
