# progetto_api/django_api_for_wagtail/admin.py
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Nation
import subprocess

def run_script(modeladmin, request, queryset):
    try:
        subprocess.run(['./add_page.sh'], cwd='path_to_your_project_directory', check=True)
        modeladmin.message_user(request, _("Script executed successfully"))
    except subprocess.CalledProcessError as e:
        modeladmin.message_user(request, _("Script execution failed with error: %s" % e), level='ERROR')

run_script.short_description = "Run add_page.sh"

@admin.register(Nation)
class NationAdmin(admin.ModelAdmin):
    list_display = ('name', 'capital')
    actions = [run_script]
