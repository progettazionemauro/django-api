from django.contrib import admin
from .models import Post
from django.shortcuts import render, redirect
from django.urls import path
from django import forms
import subprocess
import importlib
from django.apps import apps  # To check if the model is already registered
from django.db import models  # Import models from django.db

# Form for configuring the new table
class FieldConfigurationForm(forms.Form):
    field_name = forms.CharField(label='Field Name', max_length=255)
    field_type = forms.ChoiceField(choices=[('CharField', 'CharField'), ('IntegerField', 'IntegerField'), ('DateField', 'DateField')])

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'file_name', 'image_name', 'image_link')

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('create-table/', self.admin_site.admin_view(self.create_table_view), name='create_table')
        ]
        return custom_urls + urls

    def create_table_view(self, request):
        if request.method == 'POST':
            model_name = request.POST.get('model_name')
            field_forms = [FieldConfigurationForm(request.POST, prefix=str(i)) for i in range(2)]

            if all(f.is_valid() for f in field_forms) and model_name:
                # Write the new model class to models.py
                with open("blog/models.py", "a") as f:
                    f.write(f"\nclass {model_name}(models.Model):\n")
                    for f_form in field_forms:
                        field = f_form.cleaned_data
                        if field['field_type'] == 'CharField':
                            f.write(f"    {field['field_name']} = models.CharField(max_length=255)\n")
                        elif field['field_type'] == 'IntegerField':
                            f.write(f"    {field['field_name']} = models.IntegerField()\n")
                        elif field['field_type'] == 'DateField':
                            f.write(f"    {field['field_name']} = models.DateField()\n")
                    f.write(f"    def __str__(self):\n")
                    f.write(f"        return self.{field_forms[0].cleaned_data['field_name']}\n")

                # Run makemigrations and migrate to make the new table available in Django ORM
                self.run_makemigrations_and_migrate()

                # Dynamically register the new model in the admin panel
                self.register_model_in_admin(model_name)

                return redirect('admin:blog_post_changelist')

        field_forms = [FieldConfigurationForm(prefix=str(i)) for i in range(2)]
        context = {
            'field_forms': field_forms,
            'opts': self.model._meta
        }
        return render(request, 'admin/create_table.html', context)

    def run_makemigrations_and_migrate(self):
        subprocess.run(['python3', 'manage.py', 'makemigrations', 'blog'])
        subprocess.run(['python3', 'manage.py', 'migrate'])

    def register_model_in_admin(self, model_name):
        """Dynamically register the newly created model in the admin."""
        try:
            # Import the newly created model dynamically
            new_model = getattr(importlib.import_module("blog.models"), model_name)

            # Check if the model is already registered
            if not admin.site.is_registered(new_model):
                admin.site.register(new_model)
                print(f"Model {model_name} successfully registered in admin panel.")
            else:
                print(f"Model {model_name} is already registered.")
        except Exception as e:
            print(f"Error registering model {model_name}: {str(e)}")

# Function to discover models dynamically
def discover_and_register_models():
    models_module = importlib.import_module('blog.models')
    
    # Iterate over attributes in models.py to find models dynamically
    for attr_name in dir(models_module):
        attr = getattr(models_module, attr_name)
        if isinstance(attr, type) and issubclass(attr, models.Model):
            register_dynamic_model_in_admin(attr_name)

# Register dynamic models in admin
def register_dynamic_model_in_admin(model_name):
    try:
        model = getattr(importlib.import_module('blog.models'), model_name)
        admin_class = type(f'{model_name}Admin', (admin.ModelAdmin,), {'list_display': [field.name for field in model._meta.fields]})
        admin.site.register(model, admin_class)
        print(f"Successfully registered model {model_name}")
    except Exception as e:
        print(f"Failed to register model {model_name}: {str(e)}")

# Ensure models are discovered and registered
discover_and_register_models()
