# Inside populate_posts.py
from django.core.management.base import BaseCommand
from django.core.exceptions import ValidationError
from myapp.models import Post
import os

class Command(BaseCommand):
    help = 'Populate the database with posts from markdown files.'

    def handle(self, *args, **options):
        # Directory containing markdown files
        markdown_dir = "/home/mauro/Scrivania/dJANGO_apI/progetto_api/sgb_start/content/posts/"

        # List all markdown files in the directory
        markdown_files = [f for f in os.listdir(markdown_dir) if f.endswith('.md')]

        for markdown_file in markdown_files:
            try:
                # Read contents of markdown file
                with open(os.path.join(markdown_dir, markdown_file), 'r') as file:
                    content = file.read()

                # Extract title from filename
                title = os.path.splitext(markdown_file)[0]

                # Construct image_link based on the extracted title
                image_link = f"http://localhost:1313/posts/{title}/"

                # Create new Post object and save it to the database
                post = Post(
                    title=title,
                    text=content,
                    file_name=markdown_file,
                    image_name='',  # You need to provide image_name, it's not clear from where to extract it
                    image_link=image_link
                )
                post.full_clean()  # Validate the model fields
                post.save()

                self.stdout.write(self.style.SUCCESS(f"Post '{title}' saved successfully."))
            except ValidationError as e:
                self.stderr.write(self.style.ERROR(f"Validation error occurred: {e}"))
            except Exception as e:
                self.stderr.write(self.style.ERROR(f"An error occurred while processing {markdown_file}: {e}"))
