import os
import subprocess
from django.contrib import admin
from blog.models import Post, AdditionalImage  # Aggiungi AdditionalImage
from django_api_for_wagtail.models import Nation  # Importa il modello Nation

# Common actions to be inherited by all models
class CommonActionsMixin:
    def run_manage_posts_script(self, request, action, **kwargs):
        try:
            script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'sgb_start', 'manage_posts.sh'))
            env = os.environ.copy()
            env['PATH'] = '/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:' + env.get('PATH', '')

            if action in ['add', 'update']:
                result = subprocess.run(
                    [script_path, action] + list(kwargs.values()),
                    capture_output=True, text=True, check=True, env=env
                )
            elif action == 'delete':
                post_name = kwargs.get('post_name')
                result = subprocess.run(
                    [script_path, 'delete', post_name],
                    capture_output=True, text=True, check=True, env=env
                )

            if result.returncode == 0:
                self.message_user(request, "Manage posts script executed successfully")
            else:
                self.message_user(request, f"Manage posts script execution failed: {result.stderr}", level='ERROR')
        except subprocess.CalledProcessError as e:
            self.message_user(request, f"Manage posts script execution failed: {e.stderr}", level='ERROR')
        except Exception as e:
            self.message_user(request, f"Unexpected error: {e}", level='ERROR')

    def add_post_action(self, request, queryset):
        for post in queryset:
            if hasattr(post, 'file_name'):
                nation = Nation.objects.first()
                post.save()

                self.run_manage_posts_script(
                    request, 'add',
                    post_name=post.file_name.replace('.md', ''),
                    title=post.title,
                    date=post.date.strftime('%Y-%m-%dT%H:%M:%S%z'),
                    tags=post.tags,
                    categories=post.categories,
                    image=post.image_link,
                    image_alt=post.image_alt,
                    image_caption=post.image_caption,
                    nation_name=nation.name,
                    nation_capital=nation.capital
                )
            else:
                post.save()

    add_post_action.short_description = "Add New Post"

    def update_post_action(self, request, queryset):
        for post in queryset:
            if hasattr(post, 'file_name'):
                nation = Nation.objects.first()
                post.save()

                self.run_manage_posts_script(
                    request, 'update',
                    post_name=post.file_name.replace('.md', ''),
                    title=post.title,
                    date=post.date.strftime('%Y-%m-%dT%H:%M:%S%z'),
                    tags=post.tags,
                    categories=post.categories,
                    image=post.image_link,
                    image_alt=post.image_alt,
                    image_caption=post.image_caption,
                    nation_name=nation.name,
                    nation_capital=nation.capital
                )
            else:
                post.save()

    update_post_action.short_description = "Update Selected Posts"

    def delete_selected_posts(self, request, queryset):
        for post in queryset:
            try:
                if hasattr(post, 'file_name') and post.file_name:
                    self.run_manage_posts_script(request, 'delete', post_name=post.file_name.replace('.md', ''))
                post.delete()
            except Exception as e:
                self.message_user(request, f"Error deleting post '{post.title}': {e}", level='ERROR')

        self.message_user(request, "Selected posts have been deleted.")

    delete_selected_posts.short_description = "Delete Selected Posts"

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    actions = ['add_post_action', 'update_post_action', 'delete_selected_posts']


# Inline per gestire immagini aggiuntive
class AdditionalImageInline(admin.TabularInline):
    model = AdditionalImage
    extra = 1  # Mostra una riga vuota per aggiungere nuove immagini


# Register PostAdmin with the Post model
@admin.register(Post)
class PostAdmin(CommonActionsMixin, admin.ModelAdmin):
    list_display = ('title', 'file_name', 'image_name', 'image_link')
    inlines = [AdditionalImageInline]  # Aggiunge gestione inline per le immagini aggiuntive
    actions = ['add_post_action', 'update_post_action', 'delete_selected_posts']

    class Media:
        css = {
            'all': ('admin/css/custom_admin.css',)
        }


# Scoperta dinamica dei modelli
def discover_and_register_models():
    import importlib
    from django.db import models
    from django.apps import apps

    models_module = importlib.import_module('blog.models')

    for model in apps.get_models():
        if not admin.site.is_registered(model):
            register_dynamic_model_in_admin(model)


def register_dynamic_model_in_admin(model):
    try:
        admin_class = type(f'{model.__name__}Admin', (CommonActionsMixin, admin.ModelAdmin), {
            'list_display': [field.name for field in model._meta.fields]
        })
        admin.site.register(model, admin_class)
        print(f"Successfully registered model {model.__name__}")
    except Exception as e:
        print(f"Failed to register model {model.__name__}: {str(e)}")


# Scoperta e registrazione di tutti i modelli
discover_and_register_models()
