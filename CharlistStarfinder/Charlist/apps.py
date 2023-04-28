from django.apps import AppConfig


class CharlistConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Charlist'

    def ready(self):
        from . import signals