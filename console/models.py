"""console.models"""

from django.db import models
from django.urls import reverse

from core.models import Employee

MEMBER_STATUS_CHOICES = [
    ('ACTIVE', 'Active'),
    ('INACTIVE', 'Inactive'),
]


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

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Returns the url of the detail view of the model objects
        @return: The url of the detail view of the model objects
        """
        return reverse('arch-console-org-detail', kwargs={'pk': self.pk})

    class Meta:
        db_table = 'arch_console_organization'


class Team(models.Model):
    """
    Team model
    """
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=2000, blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    owners = models.ManyToManyField(Employee, through='TeamOwner', related_name='team_owners')
    members = models.ManyToManyField(Employee, through='TeamMember', related_name='team_members')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Returns the url of the detail view of the model objects
        @return: The url of the detail view of the model objects
        """
        return reverse('arch-console-org-detail', kwargs={'pk': self.pk})

    class Meta:
        db_table = 'arch_console_team'


class InvitedMember(models.Model):
    """
    Abstract model class to enable invited members
    """
    date_invited = models.DateField(auto_now_add=True)
    date_joined = models.DateField(blank=True, null=True)
    invite_code = models.CharField(blank=True, null=True, max_length=256)
    invite_accepted = models.BooleanField(default=False)
    status = models.CharField(
        max_length=20,
        choices=MEMBER_STATUS_CHOICES,
        default='INACTIVE',
    )

    class Meta:
        abstract = True


class OrganizationOwner(InvitedMember):
    """
    Organization Owner model: Many-To-Many intermediate table for Organization.owners
    """
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    class Meta:
        db_table = 'arch_console_organization_owner'


class OrganizationMember(InvitedMember):
    """
    Organization Member model: Many-To-Many intermediate table for Organization.members
    """
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    class Meta:
        db_table = 'arch_console_organization_member'


class TeamOwner(InvitedMember):
    """
    Team Owner model: Many-To-Many intermediate table for Team.owners
    """
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    class Meta:
        db_table = 'arch_console_team_owner'


class TeamMember(InvitedMember):
    """
    Team Member model: Many-To-Many intermediate table for Team.members
    """
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    class Meta:
        db_table = 'arch_console_team_member'
