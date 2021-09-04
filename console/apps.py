"""console.apps"""
from django.apps import AppConfig


class ConsoleConfig(AppConfig):
    """
    Console App Config
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'console'
