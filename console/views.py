"""console.views"""
from django.shortcuts import render
from django.views import View


class DashboardView(View):
    """
    Dashboard view
    """

    def get(self, request):
        """
        Render the dashboard.html
        """
        return render(request, 'console/dashboard.html')


class OrganizationsView(View):
    """
    Organizations view
    """

    def get(self, request):
        """
        Render the organizations.html
        """
        return render(request, 'console/organizations.html')
