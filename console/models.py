"""console.models"""

from django.db import models
from core.models import Employee


class Organization(models.Model):
    """
    Organization model
    """
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=2000, blank=True)
    owners = models.ManyToManyField(
        Employee,
        through='OrganizationOwner',
        related_name='org_owners'
    )
    members = models.ManyToManyField(
        Employee,
        through='OrganizationMember',
        related_name='org_members'
    )


class Team(models.Model):
    """
    Team model
    """
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=2000, blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    owners = models.ManyToManyField(Employee, through='TeamOwner', related_name='team_owners')
    members = models.ManyToManyField(Employee, through='TeamMember', related_name='team_members')


class OrganizationOwner(models.Model):
    """
    Organization Owner model: Many-To-Many intermediate table for Organization.owners
    """
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    date_invited = models.DateField(auto_now_add=True)
    date_joined = models.DateField(blank=True, null=True)


class OrganizationMember(models.Model):
    """
    Organization Member model: Many-To-Many intermediate table for Organization.members
    """
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    date_invited = models.DateField(auto_now_add=True)
    date_joined = models.DateField(blank=True, null=True)


class TeamOwner(models.Model):
    """
    Team Owner model: Many-To-Many intermediate table for Team.owners
    """
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    date_added = models.DateField(auto_now_add=True)


class TeamMember(models.Model):
    """
    Team Member model: Many-To-Many intermediate table for Team.members
    """
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    date_added = models.DateField(auto_now_add=True)
