# utils/admin.py

class CustomAdminSite(AdminSite):
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('run-script/', self.admin_view(run_script_view), name='run_script'),
            # Include other URL patterns from the app's urls.py
        ]
        return custom_urls + urls

custom_admin_site = CustomAdminSite(name='custom_admin')

