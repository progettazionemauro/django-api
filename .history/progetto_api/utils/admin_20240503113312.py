# utils/admin.py
from django.contrib import admin
from .views import run_script_view

@admin.register(Nation)  # Register any models from the utils app if needed
class UtilsAdmin(admin.ModelAdmin):
    pass  # You can register models from the utils app if needed

admin.site.register_view('utils/run-script/', view=run_script_view, name='run_script')  # Register the custom admin view
