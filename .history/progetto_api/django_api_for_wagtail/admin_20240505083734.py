# django_api_for_wagtail/admin.py

from django.contrib import admin
from .models import Nation, CustomFeature
import 
import subprocess

@admin.register(Nation)
class NationAdmin(admin.ModelAdmin):
    list_display = ('name', 'capital')

@admin.register(CustomFeature)
class CustomFeatureAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

    def run_script(self, request, queryset):
        try:
            os.system('python ../progetto_api/add_page.py')  # Replace with actual path
            self.message_user(request, "Script executed successfully")
        except Exception as e:  # Catch broader exceptions
            self.message_user(request, f"Script execution failed: {e}", level='ERROR')

    run_script.short_description = "Run add_page.sh"

    actions = [run_script]
