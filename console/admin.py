"""console.admin"""
from django.contrib import admin

from console.models import Organization, Team, OrganizationOwner, \
    OrganizationMember, TeamOwner, TeamMember


class BookInline(admin.TabularInline):
    """
    BookInline
    """
    model = Team


class OrganizationOwnerInline(admin.TabularInline):
    """
    OrganizationOwnerInline
    """
    model = OrganizationOwner


class OrganizationMemberInline(admin.TabularInline):
    """
    OrganizationMemberInline
    """
    model = OrganizationMember


class TeamOwnerInline(admin.TabularInline):
    """
    TeamOwnerInline
    """
    model = TeamOwner


class TeamMemberInline(admin.TabularInline):
    """
    TeamMemberInline
    """
    model = TeamMember


class OrganizationAdmin(admin.ModelAdmin):
    """
    OrganizationAdmin
    """
    inlines = [
        BookInline,
        OrganizationOwnerInline,
        OrganizationMemberInline,
    ]


class TeamAdmin(admin.ModelAdmin):
    """
    TeamAdmin
    """
    inlines = [
        TeamOwnerInline,
        TeamMemberInline,
    ]


admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Team, TeamAdmin)
