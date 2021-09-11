"""console.views.organizations"""
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from console.models import Organization
from console.services.organization import get_user_organizations, add_organization_owner


class OrganizationsView(ListView):
    """
    Organizations view
    """
    model = Organization
    template_name = 'console/organization/list.html'
    context_object_name = 'organizations'

    def get_queryset(self):
        return get_user_organizations(self.request.user.id)


class OrganizationCreateView(CreateView):
    """
    Create Organizations view
    """
    model = Organization
    fields = ['name', 'description']
    template_name = 'console/organization/create.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        add_organization_owner(self.object, self.request.user)
        return response


class OrganizationDetailView(DetailView):
    """
    Details of Organization view
    """
    model = Organization
    context_object_name = 'organization'
    template_name = 'console/organization/detail.html'


class OrganizationUpdateView(UpdateView):
    """
    Update Organizations view
    """
    model = Organization
    fields = ['name', 'description']
    template_name = 'console/organization/update.html'


class OrganizationDeleteView(DeleteView):
    """
    Delete Organizations view
    """
    model = Organization
    context_object_name = 'organization'
    template_name = 'console/organization/delete.html'
    success_url = reverse_lazy('arch-console-org-list')
