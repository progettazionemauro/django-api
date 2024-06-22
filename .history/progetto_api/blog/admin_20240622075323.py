import os
import subprocess
from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'file_name', 'image_name', 'image_link')

    def run_hello_world_script(self, request, queryset):
        try:
            current_dir = os.path.dirname(__file__)
            script_path = os.path.abspath(os.path.join(current_dir, 'hello_world.sh'))
            print("Absolute path to script:", script_path)
            
            # Ensure the script is executable
            if not os.access(script_path, os.X_OK):
                print(f"Script {script_path} is not executable")
                self.message_user(request, f"Script {script_path} is not executable", level='ERROR')
                return
            
            # Define the environment for the subprocess
            env = os.environ.copy()
            env['PATH'] = '/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:' + env.get('PATH', '')

            result = subprocess.run([script_path], capture_output=True, text=True, check=True, env=env)
            print("Script stdout:", result.stdout)
            print("Script stderr:", result.stderr)
            self.message_user(request, "Hello World script executed successfully")
        except subprocess.CalledProcessError as e:
            print("Error details:", e)
            self.message_user(request, f"Hello World script execution failed: {e.stderr}", level='ERROR')
        except Exception as e:
            print(f"Unexpected error: {e}")
            self.message_user(request, f"Unexpected error: {e}", level='ERROR')

    run_hello_world_script.short_description = "Run hello_world.sh"
    actions = [run_hello_world_script]

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

            # Define the environment for the subprocess
            env = os.environ.copy()
            env['PATH'] = '/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:' + env.get('PATH', '')

            result = subprocess.run([script_path], capture_output=True, text=True, check=True, env=env)
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
    actions = [populate_posts, run_hello_world_script]
