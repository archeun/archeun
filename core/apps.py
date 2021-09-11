"""core.apps"""
from django.apps import AppConfig


class CoreConfig(AppConfig):
    """
    Core App Config
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
