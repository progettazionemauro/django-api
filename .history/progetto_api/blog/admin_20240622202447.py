import os
import subprocess
from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'file_name', 'image_name', 'image_link')

    def run_add_page_script(self, request, queryset):
        try:
            current_dir = os.path.dirname(__file__)
            script_path = os.path.abspath(os.path.join(current_dir, 'add_page.sh'))
            print("Absolute path to script:", script_path)

            # Ensure the script is executable
            if not os.access(script_path, os.X_OK):
                print(f"Script {script_path} is not executable")
                self.message_user(request, f"Script {script_path} is not executable", level='ERROR')
                return

            # Define the environment for the subprocess
            env = os.environ.copy()
            env['PATH'] = '/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:' + env.get('PATH', '')

            for obj in queryset:
                result = subprocess.run([script_path, "create"], capture_output=True, text=True, check=True, env=env)
                print("Script stdout:", result.stdout)
                print("Script stderr:", result.stderr)

            self.message_user(request, "Add page script executed successfully")
        except subprocess.CalledProcessError as e:
            print("Error details:", e)
            self.message_user(request, f"Add page script execution failed: {e.stderr}", level='ERROR')
        except Exception as e:
            print(f"Unexpected error: {e}")
            self.message_user(request, f"Unexpected error: {e}", level='ERROR')

    def run_delete_page_script(self, request, queryset):
        try:
            current_dir = os.path.dirname(__file__)
            script_path = os.path.abspath(os.path.join(current_dir, 'add_page.sh'))
            print("Absolute path to script:", script_path)

            # Ensure the script is executable
            if not os.access(script_path, os.X_OK):
                print(f"Script {script_path} is not executable")
                self.message_user(request, f"Script {script_path} is not executable", level='ERROR')
                return

            # Define the environment for the subprocess
            env = os.environ.copy()
            env['PATH'] = '/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:' + env.get('PATH', '')

            for obj in queryset:
                result = subprocess.run([script_path, "delete", obj.file_name], capture_output=True, text=True, check=True, env=env)
                print("Script stdout:", result.stdout)
                print("Script stderr:", result.stderr)

            self.message_user(request, "Delete page script executed successfully")
        except subprocess.CalledProcessError as e:
            print("Error details:", e)
            self.message_user(request, f"Delete page script execution failed: {e.stderr}", level='ERROR')
        except Exception as e:
            print(f"Unexpected error: {e}")
            self.message_user(request, f"Unexpected error: {e}", level='ERROR')

    run_add_page_script.short_description = "Run add_page.sh to create a post"
    run_delete_page_script.short_description = "Run add_page.sh to delete a post"

    actions = [run_add_page_script, run_delete_page_script]
