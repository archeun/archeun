"""console.views.organizations"""
from django.shortcuts import render
from django.views import View

from console.services.organization import get_user_organizations


class OrganizationsView(View):
    """
    Organizations view
    """

    def get(self, request):
        """
        Render the organizations.html
        This view will render the CRUD panel for the Organization entity
        inside a single page
        """
        organizations = get_user_organizations(request.user.id)
        return render(
            request,
            'console/organization/organizations.html',
            context={'organizations': organizations}
        )
