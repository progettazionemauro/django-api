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

    


    run_script.short_description = "Run add_page.sh"

    actions = [run_script]
