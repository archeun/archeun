"""console.models"""

from django.db import models
from django.urls import reverse

from core.models import Employee

MEMBER_STATUS_CHOICES = [
    ('ACTIVE', 'Active'),
    ('INACTIVE', 'Inactive'),
]

INVITE_TYPE_CHOICES = [
    ('ORG_OWNER', 'Organization Owner'),
    ('ORG_MEMBER', 'Organization Member'),
]

INVITE_STATUS_CHOICES = [
    ('PENDING', 'Pending'),
    ('ACCEPTED', 'Accepted'),
    ('REJECTED', 'Rejected'),
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


class JoinedMember(models.Model):
    """
    Abstract model class to enable joined member attributes
    """
    date_joined = models.DateField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=MEMBER_STATUS_CHOICES,
        default='INACTIVE',
    )

    class Meta:
        abstract = True


class OrganizationOwner(JoinedMember):
    """
    Organization Owner model: Many-To-Many intermediate table for Organization.owners
    """
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    class Meta:
        db_table = 'arch_console_organization_owner'


class OrganizationMember(JoinedMember):
    """
    Organization Member model: Many-To-Many intermediate table for Organization.members
    """
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    class Meta:
        db_table = 'arch_console_organization_member'


class TeamOwner(JoinedMember):
    """
    Team Owner model: Many-To-Many intermediate table for Team.owners
    """
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    class Meta:
        db_table = 'arch_console_team_owner'


class TeamMember(JoinedMember):
    """
    Team Member model: Many-To-Many intermediate table for Team.members
    """
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    class Meta:
        db_table = 'arch_console_team_member'


class EmailInvite(models.Model):
    """
    Email Invite model: Model to store all email invites in the system
    """

    email = models.EmailField()
    invite_type = models.CharField(
        max_length=20,
        choices=INVITE_TYPE_CHOICES,
    )
    invited_date = models.DateTimeField()
    invite_accepted_date = models.DateTimeField()
    status = models.CharField(
        max_length=20,
        choices=INVITE_STATUS_CHOICES,
        default='PENDING',
    )

    class Meta:
        db_table = 'arch_console_email_invite'
