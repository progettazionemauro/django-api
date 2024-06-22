# utils/views.py
from django import admin
from django.http import HttpResponse
import subprocess

def run_script_view(request):
    try:
        subprocess.run(['./add_page.sh'], cwd='path_to_your_project_directory', check=True)
        return HttpResponse("Script executed successfully")
    except subprocess.CalledProcessError as e:
        return HttpResponse("Script execution failed with error: %s" % e, status=500)
