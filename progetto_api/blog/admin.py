import os
import subprocess
from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'file_name', 'image_name', 'image_link')

    def run_manage_posts_script(self, request, queryset, action, **kwargs):
        try:
            script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'sgb_start', 'manage_posts.sh'))
            env = os.environ.copy()
            env['PATH'] = '/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:' + env.get('PATH', '')

            if action == 'add':
                post_name = kwargs.get('post_name')
                title = kwargs.get('title')
                date = kwargs.get('date')
                tags = kwargs.get('tags')
                categories = kwargs.get('categories')
                image = kwargs.get('image')
                image_alt = kwargs.get('image_alt')
                image_caption = kwargs.get('image_caption')

                result = subprocess.run(
                    [script_path, 'add', post_name, title, date, tags, categories, image, image_alt, image_caption],
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
            post_name = post.title.replace(' ', '_').lower() + '.md'
            title = post.title
            date = post.date.strftime('%Y-%m-%dT%H:%M:%S%z')
            tags = post.tags
            categories = post.categories
            image = post.image_name
            image_alt = post.image_alt
            image_caption = post.image_caption

            self.run_manage_posts_script(
                request, queryset, 'add',
                post_name=post_name,
                title=title,
                date=date,
                tags=tags,
                categories=categories,
                image=image,
                image_alt=image_alt,
                image_caption=image_caption
            )

    add_post_action.short_description = "Add a new post"
    actions = [add_post_action]

    def delete_model(self, request, obj):
        self.run_manage_posts_script(request, None, 'delete', post_name=obj.file_name)

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
