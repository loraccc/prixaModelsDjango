from django.apps import AppConfig


class ModeltypeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'modelType'

    def ready(self):
        import modelType.signals





