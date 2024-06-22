import os
import subprocess
from django.contrib import admin
from .models import CustomFeature, Post

@admin.register(CustomFeature)
class CustomFeatureAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

    def run_script(self, request, queryset):
        try:
            current_dir = os.path.dirname(__file__) 
            script_path = os.path.abspath(os.path.join(current_dir, 'add_page.sh'))
            print("Absolute path to script:", script_path)
            
            # Ensure the script is executable
            if not os.access(script_path, os.X_OK):
                print(f"Script {script_path} is not executable")
                self.message_user(request, f"Script {script_path} is not executable", level='ERROR')
                return
            
            result = subprocess.run([script_path], capture_output=True, text=True, check=True, env=os.environ.copy())
            print("Script stdout:", result.stdout)
            print("Script stderr:", result.stderr)
            self.message_user(request, "Script executed successfully")
        except subprocess.CalledProcessError as e:
            print("Error details:", e)
            self.message_user(request, f"Script execution failed: {e.stderr}", level='ERROR')
        except Exception as e:
            print(f"Unexpected error: {e}")
            self.message_user(request, f"Unexpected error: {e}", level='ERROR')

    run_script.short_description = "Run add_page.sh"
    actions = [run_script]

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'file_name', 'image_name', 'image_link')

    def populate_posts(self, request, queryset):
        try:
            current_dir = os.path.dirname(__file__)
            script_path = os.path.abspath(os.path.join(current_dir, 'populate_posts.sh'))
            print("Absolute path to script:", script_path)
            
            # Ensure the script is executable
            if not os.access(script_path, os.X_OK):
                print(f"Script {script_path} is not executable")
                self.message_user(request, f"Script {script_path} is not executable", level='ERROR')
                return

            result = subprocess.run([script_path], capture_output=True, text=True, check=True, env=os.environ.copy())
            print("Script stdout:", result.stdout)
            print("Script stderr:", result.stderr)
            self.message_user(request, "Posts populated successfully")
        except subprocess.CalledProcessError as e:
            print("Error details:", e)
            self.message_user(request, f"Failed to populate posts: {e.stderr}", level='ERROR')
        except Exception as e:
            print(f"Unexpected error: {e}")
            self.message_user(request, f"Unexpected error: {e}", level='ERROR')

    populate_posts.short_description = "Run populate_posts.sh"
    actions = [populate_posts]
