# django_api_for_wagtail/admin.py

from django.contrib import admin
from .models import Nation, CustomFeature
import os
import subprocess

@admin.register(Nation)
class NationAdmin(admin.ModelAdmin):
    list_display = ('name', 'capital')

@admin.register(CustomFeature)
class CustomFeatureAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

    def run_script(self, request, queryset):
        try:
            current_dir = os.path.dirname(__file__)
            script_path = os.path.join(current_dir, '..', '..', 'progetto_api', 'add_page.sh')
            subprocess.run([script_path], check=True)
            self.message_user(request, "Script executed successfully")
        except Exception as e:
            self.message_user(request, f"Script execution failed: {e}", level='ERROR')


    run_script.short_description = "Run add_page.sh"

    actions = [run_script]
