from django.apps import AppConfig

class DjangoApiForWagtailConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_api_for_wagtail'
    
    def ready(self):
        import django_api_for_wagtail.signals
