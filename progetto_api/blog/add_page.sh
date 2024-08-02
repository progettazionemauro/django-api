import os
import subprocess
from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'file_name', 'image_name', 'image_link')

    def run_manage_posts_script(self, request, queryset):
        try:
            current_dir = os.path.dirname(__file__)
            script_path = os.path.abspath(os.path.join(current_dir, '..', 'sgb_start', 'manage_posts.sh'))
            print("Absolute path to script:", script_path)
            
            # Ensure the script is executable
            if not os.access(script_path, os.X_OK):
                print(f"Script {script_path} is not executable")
                self.message_user(request, f"Script {script_path} is not executable", level='ERROR')
                return
            
            # Define the environment for the subprocess
            env = os.environ.copy()
            env['PATH'] = '/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:' + env.get('PATH', '')

            # Add or delete a post based on the user's input
            action = input("Enter 'add' to create a new post or 'delete' to delete a post: ").strip().lower()
            if action == 'add':
                result = subprocess.run([script_path, 'add'], capture_output=True, text=True, check=True, env=env)
            elif action == 'delete':
                result = subprocess.run([script_path, 'delete'], capture_output=True, text=True, check=True, env=env)
            else:
                print("Invalid action. Please enter 'add' or 'delete'.")
                return

            print("Script stdout:", result.stdout)
            print("Script stderr:", result.stderr)
            self.message_user(request, "Manage posts script executed successfully")
        except subprocess.CalledProcessError as e:
            print("Error details:", e)
            self.message_user(request, f"Manage posts script execution failed: {e.stderr}", level='ERROR')
        except Exception as e:
            print(f"Unexpected error: {e}")
            self.message_user(request, f"Unexpected error: {e}", level='ERROR')

    run_manage_posts_script.short_description = "Run manage_posts.sh"
    actions = [run_manage_posts_script]

