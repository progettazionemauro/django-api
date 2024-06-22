# utils/management/commands/run_script.py
from django.core.management.base import BaseCommand
import subprocess

class Command(BaseCommand):
    help = 'Runs the add_page.sh script'

    def handle(self, *args, **kwargs):
        try:
            subprocess.run(['./add_page.sh'], cwd='path_to_your_project_directory', check=True)
            self.stdout.write(self.style.SUCCESS('Script executed successfully'))
        except subprocess.CalledProcessError as e:
            self.stdout.write(self.style.ERROR(f'Script execution failed with error: {e}'))
