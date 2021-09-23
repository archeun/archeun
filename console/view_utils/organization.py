"""console.view_utils.organization"""
from django.db.models import Q
from console.models import OrganizationInvite


def get_organization_owners_for_list(organization):
    """
    Returns the owners list of the given organization to be represented in the list
    @param organization:
    @return:
    """
    owners = []
    for owner in organization.organizationowner_set.all():
        owners.append({
            'Name': '{first} {last}'.format(
                first=owner.employee.user.first_name,
                last=owner.employee.user.last_name
            ),
            'Email': owner.employee.user.email,
            'Date Joined': owner.date_joined,
        })

    return owners


def get_organization_members_for_list(organization):
    """
    Returns the members list of the given organization to be represented in the list
    @param organization:
    @return:
    """
    members = []
    for member in organization.organizationmember_set.all():
        members.append({
            'Name': '{first} {last}'.format(
                first=member.employee.user.first_name,
                last=member.employee.user.last_name
            ),
            'Email': member.employee.user.email,
            'Date Joined': member.date_joined,
        })

    return members


def get_organization_invites_by_type_for_list(organization, invite_type):
    """
    Returns the owner invites list of the given organization to be represented in the list

    @param invite_type:
    @type organization: Organization
    @param organization:
    @return:
    """

    invite_set = organization.organizationinvite_set.filter(
        Q(status=OrganizationInvite.ORG_INVITE_STATUS_PENDING) |
        Q(status=OrganizationInvite.ORG_INVITE_STATUS_REJECTED),
        invite_type=invite_type
    )
    invites = []
    for invite in invite_set:
        invites.append({
            'Email': invite.email,
            'Invited Date/time': invite.invited_date_time,
            'Status': invite.status,
        })

    return invites
