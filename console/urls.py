"""console.urls"""
from django.urls import path

from console.views.dashboard import DashboardView
from console.views.organization import OrganizationsView

urlpatterns = [

    path(
        '',
        DashboardView.as_view(), name='arch-console-dashboard'
    ),

    path(
        'o/',
        OrganizationsView.as_view(), name='arch-console-orgs'
    ),

]
