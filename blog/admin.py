
from django.contrib import admin
from .models import CustomFeature
import os
import subprocess
from .models import Post

@admin.register(CustomFeature)
class CustomFeatureAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

    def run_script(self, request, queryset):
        try:
            # This line retrieves the directory path of the current Python script (admin.py in this case) using __file__, 
            # which is a special attribute in Python that represents the current file path.
            current_dir = os.path.dirname(__file__) 
            script_path = os.path.abspath(os.path.join(current_dir, 'add_page.sh'))
            print("Absolute path to script:", script_path)  # Print out the absolute path
            subprocess.run([script_path], check=True)
            self.message_user(request, "Script executed successfully")
        except Exception as e:
            self.message_user(request, f"Script execution failed: {e}", level='ERROR')


    run_script.short_description = "Run add_page.sh"

    actions = [run_script]
    
    from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'file_name', 'image_name', 'image_link')

    def populate_posts(self, request, queryset):
        try:
            current_dir = os.path.dirname(__file__)
            script_path = os.path.abspath(os.path.join(current_dir, 'populate_posts.sh'))
            subprocess.run([script_path], check=True)
            self.message_user(request, "Posts populated successfully")
        except Exception as e:
            self.message_user(request, f"Failed to populate posts: {e}", level='ERROR')

    populate_posts.short_description = "Run populate_posts.sh"
    actions = [populate_posts]
