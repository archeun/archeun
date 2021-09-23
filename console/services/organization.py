"""
Service layer to handle business logic related to Organizations
"""
# pylint: disable=imported-auth-user
from django.contrib.auth.models import User
from django.db.models import QuerySet

from console.models import Organization, OrganizationOwner, OrganizationInvite


def get_user_organizations(user_id: int) -> QuerySet:
    """
    Returns the set of organizations where the given user's employee is an owner of

    Arguments:
        user_id (int): User id

    Returns:
        QuerySet: The set of organizations where the given user's employee is an owner of

    Raises:
    """
    return Organization.objects.filter(owners__user_id=user_id).all()


def add_organization_owner(organization: Organization, user: User) -> Organization:
    """
    Adds the employee of the given user as the owner to the given organization

    Arguments:
        organization (Organization): Organization object to add the owner
        user (User): User to be added as the owner

    Returns:
        Organization: The Organization with the owner added

    Raises:
    """
    owner = OrganizationOwner()
    owner.employee = user.employee
    owner.organization = organization
    owner.save()
    organization.organizationowner_set.add(owner)
    return organization


def invite_organization_owners(organization, emails):
    """
    Service entry point to invite organization owners
    @param Organization organization: The organization object
    @param emails: The list of emails to be invited as owners
    @return:
    """
    create_organization_invites(organization, emails, OrganizationInvite.ORG_INVITE_TYPE_OWNER)


def create_organization_invites(organization, emails, invite_type):
    """
    Creates OrganizationInvites with the given emails for the given organization and type
    @param Organization organization: The organization object
    @param emails: The list of emails to be invited
    @param invite_type: Type of invite
    @return:
    """
    invited_emails = get_organization_invite_emails(organization)
    for email in emails:
        if email not in invited_emails:
            organization_invite = OrganizationInvite()
            organization_invite.organization_id = organization.id
            organization_invite.email = email
            organization_invite.invite_type = invite_type
            organization_invite.status = OrganizationInvite.ORG_INVITE_STATUS_PENDING
            organization_invite.save()


def get_organization_invite_emails(organization):
    """
    Returns the organization invited emails for the given organization
    @param Organization organization:
    @return: []
    """
    return list(
        organization.organizationinvite_set.values_list(
            'email',
            flat=True
        )
    )
