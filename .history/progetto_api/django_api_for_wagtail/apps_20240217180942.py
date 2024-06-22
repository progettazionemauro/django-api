from django.apps import AppConfig
import django_api_for_wagtail.signals  # Make sure the signals are imported

class DjangoApiForWagtailConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "django_api_for_wagtail"
    
    def ready(self):
        # Print a debug message to verify that the ready() method is being called
        print("Django API for Wagtail app is ready!")

        # Import signals to ensure they are registered when Django starts up
        import django_api_for_wagtail.signals
