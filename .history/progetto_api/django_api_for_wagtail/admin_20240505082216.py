# django_api_for_wagtail/admin.py

from django.contrib import admin
from .models import Nation, CustomFeature
import subprocess

@admin.register(Nation)
class NationAdmin(admin.ModelAdmin):
    list_display = ('name', 'capital')

@admin.register(CustomFeature)
class CustomFeatureAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

    def run_script(self, request, queryset):
        try:
            subprocess.run(['../progettoadd_page.sh'], cwd='../progetto_api', check=True)
            self.message_user(request, "Script executed successfully")
        except subprocess.CalledProcessError as e:
            self.message_user(request, f"Script execution failed with error: {e}", level='ERROR')

    run_script.short_description = "Run add_page.sh"

    actions = [run_script]
