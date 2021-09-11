"""console.urls"""
from django.urls import path
from console import views as arch_console_views

urlpatterns = [

    path(
        '',
        arch_console_views.DashboardView.as_view(), name='arch-console-dashboard'
    ),

    path(
        'o/',
        arch_console_views.OrganizationsView.as_view(), name='arch-console-orgs'
    ),

]
