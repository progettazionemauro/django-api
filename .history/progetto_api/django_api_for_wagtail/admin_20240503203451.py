# django_api_for_wagtail/admin.py
from django.contrib import admin
from .models import Nation

@admin.register(Nation)
class NationAdmin(admin.ModelAdmin):
    list_display = ('name', 'capital', 'custom_text')  # Add 'custom_text' here

    def custom_text(self, obj):
        return "Custom Text Here"  # Modify this to display your desired text

    custom_text.short_description = 'Custom Text'  # Set a short description for the column header