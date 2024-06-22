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
        # This line retrieves the directory path of the current Python script (admin.py in this case) using __file__, 
        # which is a special attribute in Python that represents the current file path.
        current_dir = os.path.dirname(__file__) 
        script_path = os.path.abspath(os.path.join(current_dir, 'add_page.sh'))
        print("Absolute path to script:", script_path)  # Print out the absolute path

        # Capture script output and errors
        result = subprocess.run([script_path], capture_output=True, text=True)

        if result.returncode == 0:
            self.message_user(request, "Script executed successfully")
        else:
            error_message = result.stderr.strip() if result.stderr else "Unknown error"
            self.message_user(request, f"Script execution failed: {error_message}", level='ERROR')
        except Exception as e:
            self.message_user(request, f"Script execution failed: {e}", level='ERROR')


    run_script.short_description = "Run add_page.sh"

    actions = [run_script]
