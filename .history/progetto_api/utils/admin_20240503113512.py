# utils/admin.py
from django.contrib.admin import AdminSite
from django.http import HttpResponse
from .views import run_script_view

class UtilsAdminSite(AdminSite):
    def run_script(self, request):
        # Call your custom view function
        return run_script_view(request)

utils_admin_site = UtilsAdminSite(name='utils_admin')
