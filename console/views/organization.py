"""console.views.organizations"""
# pylint: disable=no-self-use
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, FormView

from console.forms import MultiEmailInviteForm
from console.models import Organization, OrganizationInvite
from console.services.organization import get_user_organizations, \
    add_organization_owner, \
    invite_organization_owners, invite_organization_members
from console.view_utils.organization import get_organization_owners_for_list, \
    get_organization_members_for_list, get_organization_invites_by_type_for_list
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
            'Date Joined',
        ],
        'members': [
            'Name',
            'Email',
            'Date Joined',
        ],
        'owner_invites': [
            'Email',
            'Invited Date/time',
            'Status',
        ],
        'member_invites': [
            'Email',
            'Invited Date/time',
            'Status',
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
        organization = self.get_object()
        return {
            'owners': get_organization_owners_for_list(organization),
            'members': get_organization_members_for_list(organization),
            'owner_invites': get_organization_invites_by_type_for_list(
                organization,
                OrganizationInvite.ORG_INVITE_TYPE_OWNER
            ),
            'member_invites': get_organization_invites_by_type_for_list(
                organization,
                OrganizationInvite.ORG_INVITE_TYPE_MEMBER
            ),
        }


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
    template_name = 'console/organization/invite.html'
    form_class = MultiEmailInviteForm
    success_url = reverse_lazy('arch-console-org-list')
    organization = None
    invite_type = 'Owners'

    def get_context_data(self, **kwargs):
        """Insert the form into the context dict."""
        kwargs['invite_type'] = self.invite_type
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

    def persist_invites(self, organization, emails):
        """
        Saves the invites for given emails under the given org
        @param organization:
        @param emails:
        @return:
        """
        invite_organization_owners(organization, emails)

    def form_valid(self, form):
        """If the form is valid, send out emails"""
        self.persist_invites(self.organization, form.get_email_list())
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("arch-console-org-detail", kwargs={'pk': self.organization.id})


class OrganizationInviteMembersView(OrganizationInviteOwnersView):
    """
    Form view to invite members to the organization by emails
    """
    invite_type = 'Members'

    def persist_invites(self, organization, emails):
        """
        Saves the invites for given emails under the given org
        @param organization:
        @param emails:
        @return:
        """
        invite_organization_members(organization, emails)
