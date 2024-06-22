from django.apps import AppConfig

class DjangoApiForWagtailConfig(AppConfig):
    # Set the name of your app
    name = "django_api_for_wagtail"

    # Optionally, you can specify a custom default auto field
    # (if you're using Django 3.2 or later)
    default_auto_field = "django.db.models.BigAutoField"

    # Add any other configurations or customizations specific to your app here
    # ...

    # The 'ready' method is called when the app is loaded.
    # You can use it to connect signals, register custom management commands, etc.
    def ready(self):
        # Import and connect your signals here (if you have any)
        # Example: from . import signals
        pass
