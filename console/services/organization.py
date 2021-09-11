"""
Service layer to handle business logic related to Organizations
"""
from django.db.models import QuerySet

from console.models import Organization


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
