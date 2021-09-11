"""core.models"""
# pylint: disable=imported-auth-user
from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    """
    User profile model by extending the User model
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'arch_core_user_profile'
