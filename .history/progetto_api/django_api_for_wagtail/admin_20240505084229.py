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

    import subprocess

def run_script(self, request, queryset):
    try:
        # Capture output using shell=True and capture_output=True
        result = subprocess.run(['./../progetto_api/add_page.sh'], shell=True, capture_output=True)
        output = result.stdout.decode()  # Decode captured output

        # Check for success and display appropriate message
        if result.returncode == 0:
            self.message_user(request, f"Script executed successfully.\nOutput:\n{output}")
        else:
            self.message_user(request, f"Script execution failed with error code: {result.returncode}\nOutput:\n{output}", level='ERROR')
    except Exception as e:
        self.message_user(request, f"Script execution failed: {e}", level='ERROR')


    run_script.short_description = "Run add_page.sh"

    actions = [run_script]
