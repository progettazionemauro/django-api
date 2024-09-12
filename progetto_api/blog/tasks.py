from __future__ import absolute_import, unicode_literals
from celery import shared_task
import os
import subprocess

@shared_task
def run_manage_posts_script_task(action, post_name, title, date, tags, categories, image, image_alt, image_caption, nation_name, nation_capital):
    try:
        script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'sgb_start', 'manage_posts.sh'))
        env = os.environ.copy()
        env['PATH'] = '/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:' + env.get('PATH', '')

        if action in ['add', 'update']:
            subprocess.run(
                [script_path, action, post_name, title, date, tags, categories, image, image_alt, image_caption, nation_name, nation_capital],
                capture_output=True, text=True, check=True, env=env
            )
        elif action == 'delete':
            subprocess.run(
                [script_path, 'delete', post_name],
                capture_output=True, text=True, check=True, env=env
            )
    except subprocess.CalledProcessError as e:
        print(f"Errore durante l'esecuzione dello script: {e.stderr}")
    except Exception as e:
        print(f"Errore imprevisto: {e}")
