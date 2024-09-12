from django.contrib import admin
from .models import Post, TableConfiguration, FieldConfiguration
from django.shortcuts import render, redirect
from django.urls import path
from django import forms
import subprocess

# Form per la configurazione della nuova tabella
class TableConfigurationForm(forms.ModelForm):
    class Meta:
        model = TableConfiguration
        fields = ['table_name']

class FieldConfigurationForm(forms.ModelForm):
    class Meta:
        model = FieldConfiguration
        fields = ['field_name', 'field_type']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'file_name', 'image_name', 'image_link')

@admin.register(TableConfiguration)
class TableConfigurationAdmin(admin.ModelAdmin):
    list_display = ('table_name', 'created_at')

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('create-table/', self.admin_site.admin_view(self.create_table_view), name='create_table')
        ]
        return custom_urls + urls

    def create_table_view(self, request):
        if request.method == 'POST':
            form = TableConfigurationForm(request.POST)
            field_forms = [FieldConfigurationForm(request.POST, prefix=str(i)) for i in range(3)]  # Limite di 3 campi

            if form.is_valid() and all(f.is_valid() for f in field_forms):
                table = form.save()
                for f in field_forms:
                    field = f.save(commit=False)
                    field.table = table
                    field.save()

                # Avvia migrazione
                subprocess.run(['python3', 'manage.py', 'makemigrations', 'blog'])
                subprocess.run(['python3', 'manage.py', 'migrate'])

                return redirect('admin:blog_tableconfiguration_changelist')
        else:
            form = TableConfigurationForm()
            field_forms = [FieldConfigurationForm(prefix=str(i)) for i in range(3)]

        context = {
            'form': form,
            'field_forms': field_forms,
            'opts': self.model._meta
        }

        return render(request, 'admin/create_table.html', context)
