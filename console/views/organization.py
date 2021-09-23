"""console.views.organizations"""
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, FormView

from console.forms import MultiEmailInviteForm
from console.models import Organization
from console.services.organization import get_user_organizations, \
    add_organization_owner, \
    invite_organization_owners
from core.mixins import ArchItemListViewMixin


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


class OrganizationDetailView(ArchItemListViewMixin, DetailView):
    """
    Details of Organization view
    """
    model = Organization
    context_object_name = 'organization'
    template_name = 'console/organization/detail.html'
    list_headers = {
        'owners': [
            'Name',
            'Email',
            'Date Invited',
            'Date Joined',
        ],
        'members': [
            'Name',
            'Email',
            'Date Invited',
            'Date Joined',
        ],
    }

    def get_context_data(self, **kwargs):
        """
        Returns the context data
        @param kwargs:
        @return:
        """
        context = super().get_context_data(**kwargs)
        list_context_data = super().get_list_context_data()
        context = {**context, **list_context_data}
        return context

    def get_list_items(self):
        """
        Returns the items for the list as an array
        @return:
        """
        items = {'owners': [], 'members': []}
        organization = self.get_object()
        for owner in organization.organizationowner_set.all():
            items['owners'].append({
                'Name': '{first} {last}'.format(
                    first=owner.employee.user.first_name,
                    last=owner.employee.user.last_name
                ),
                'Email': owner.employee.user.email,
                'Date Invited': owner.date_invited,
                'Date Joined': owner.date_joined,
            })
        for member in organization.organizationmember_set.all():
            items['members'].append({
                'Name': '{first} {last}'.format(
                    first=member.employee.user.first_name,
                    last=member.employee.user.last_name
                ),
                'Email': member.employee.user.email,
                'Date Invited': member.date_invited,
                'Date Joined': member.date_joined,
            })
        return items


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


class OrganizationInviteOwnersView(FormView):
    """
    Form view to invite owners to the organization by emails
    """
    template_name = 'console/organization/owner/invite.html'
    form_class = MultiEmailInviteForm
    success_url = reverse_lazy('arch-console-org-list')
    organization = None

    def get_context_data(self, **kwargs):
        """Insert the form into the context dict."""
        if 'organization' not in kwargs:
            kwargs['organization'] = self.organization
        return super().get_context_data(**kwargs)

    def get(self, request, *args, **kwargs):
        """
        Initialize the organization object for GET
        @param request:
        @param args:
        @param kwargs:
        @return:
        """
        self.organization = get_object_or_404(Organization, pk=kwargs['pk'])
        return super().get(request, args, kwargs)

    def post(self, request, *args, **kwargs):
        """
        Initialize the organization object for POST
        @param request:
        @param args:
        @param kwargs:
        @return:
        """
        self.organization = get_object_or_404(Organization, pk=kwargs['pk'])
        return super().post(request, args, kwargs)

    def form_valid(self, form):
        """If the form is valid, send out emails"""
        invite_organization_owners(self.organization, form.get_email_list())
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("arch-console-org-detail", kwargs={'pk': 1})
