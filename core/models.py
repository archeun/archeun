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
