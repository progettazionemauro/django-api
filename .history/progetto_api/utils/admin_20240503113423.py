# utils/admin.py
from django.contrib import admin
from .views import run_script_view

admin.site.register_view('utils/run-script/', view=run_script_view, name='run_script')
