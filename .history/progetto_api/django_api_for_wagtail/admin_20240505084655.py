from django.contrib import admin
from .models import Nation, CustomFeature
import subprocess
import os

@admin.register(Nation)
class NationAdmin(admin.ModelAdmin):
    list_display = ('name', 'capital')

@admin.register(CustomFeature)
class CustomFeatureAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

    def run_script(self, request, queryset):
        # Get the directory path of the current file
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Construct the full path to the script
        script_path = os.path.join(script_dir, '..', 'progetto_api', 'add_page.sh')

        try:
            # Execute the script and capture its output
            result = subprocess.run([script_path], check=True, capture_output=True, text=True)
            # Display the output as a message
            self.message_user(request, result.stdout)
        except subprocess.CalledProcessError as e:
            # If an error occurs, display the error message
            self.message_user(request, f"Script execution failed with error: {e.stderr}", level='ERROR')

    run_script.short_description = "Run add_page.sh"

    actions = [run_script]
