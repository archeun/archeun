"""
Service layer to handle business logic related to Organizations
"""
# pylint: disable=imported-auth-user
from django.contrib.auth.models import User
from django.db.models import QuerySet

from console.models import Organization, OrganizationOwner


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
