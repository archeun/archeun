"""console.views.organizations"""
from django.views.generic import ListView

from console.models import Organization
from console.services.organization import get_user_organizations


class OrganizationsView(ListView):
    """
    Organizations view
    """
    model = Organization
    template_name = 'console/organization/organizations.html'
    context_object_name='organizations'

    def get_queryset(self):
        return get_user_organizations(self.request.user.id)
