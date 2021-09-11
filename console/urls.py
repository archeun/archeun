"""console.urls"""
from django.urls import path

from console.views.dashboard import DashboardView
from console.views.organization import OrganizationsView, OrganizationCreateView, \
    OrganizationDetailView, OrganizationUpdateView, OrganizationDeleteView

urlpatterns = [

    path(
        '',
        DashboardView.as_view(), name='arch-console-dashboard'
    ),

    path(
        'o/',
        OrganizationsView.as_view(), name='arch-console-org-list'
    ),

    path(
        'o/create',
        OrganizationCreateView.as_view(), name='arch-console-org-create'
    ),

    path(
        'o/detail/<int:pk>/',
        OrganizationDetailView.as_view(), name='arch-console-org-detail'
    ),

    path(
        'o/update/<int:pk>/',
        OrganizationUpdateView.as_view(), name='arch-console-org-update'
    ),

    path(
        'o/delete/<int:pk>/',
        OrganizationDeleteView.as_view(), name='arch-console-org-delete'
    ),

]
