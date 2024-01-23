# django_api_for_wagtail/admin.py
from django.contrib import admin
from .models import Nation

@admin.register(Nation)
class NationAdmin(admin.ModelAdmin):
    list_display = ('name', 'capital')