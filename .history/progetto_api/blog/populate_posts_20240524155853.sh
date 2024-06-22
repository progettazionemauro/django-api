#!/bin/bash

# Directory containing markdown files
markdown_dir="/home/mauro/Scrivania/dJANGO_apI/progetto_api/sgb_start/content/posts/"

# Output file to store processed file details
output_file="/home/mauro/Scrivania/dJANGO_apI/progetto_api/blog/processed_files.txt"

# Check if the directory exists
if [ ! -d "$markdown_dir" ]; then
  echo "Error: Directory $markdown_dir does not exist."
  exit 1
fi

# Create or clear the output file
> "$output_file"

# Collect existing files
existing_files=()
for markdown_file in "$markdown_dir"/*.md; do
  if [ -f "$markdown_file" ]; then
    existing_files+=("$(basename -- "$markdown_file")")
  fi
done

# Join existing files into a comma-separated string
existing_files_str=$(IFS=,; echo "${existing_files[*]}")

# Django shell commands to update or create posts and delete missing posts
django_commands=$(cat <<EOF
from blog.models import Post

# Collect existing files from the script
existing_files = ["${existing_files_str}"]

# Update or create posts from markdown files
for filename in existing_files:
    title = filename.split('.')[0]
    content_file = f"${markdown_dir}/{filename}"
    with open(content_file, 'r') as file:
        content = file.read().replace('"', '\\"').replace("'", "\\'")
    
    image_link = f"http://localhost:1313/posts/{title}/"
    
    post, created = Post.objects.update_or_create(
        file_name=filename,
        defaults={
            'title': title,
            'text': content,
            'image_name': '',
            'image_link': image_link
        }
    )

# Delete posts that no longer have corresponding markdown files
Post.objects.exclude(file_name__in=existing_files).delete()
EOF
)

# Print the details (for demonstration purposes)
for markdown_file in "$markdown_dir"/*.md; do
  if [ -f "$markdown_file" ]; then
    # Read contents of the markdown file and escape problematic characters
    content=$(cat "$markdown_file" | sed 's/"/\\"/g' | sed "s/'/\\'/g" | tr '\n' ' ')

    # Extract title from filename
    filename=$(basename -- "$markdown_file")
    title="${filename%.*}"

    # Construct image_link based on the extracted title
    image_link="http://localhost:1313/posts/${title}/"

    echo "Title: $title"
    echo "File Name: $filename"
    echo "Content: $content"
    echo "Image Link: $image_link"
    echo "-------------------------"

    # Log the details to the output file
    echo "Title: $title" >> "$output_file"
    echo "File Name: $filename" >> "$output_file"
    echo "Content: $content" >> "$output_file"
    echo "Image Link: $image_link" >> "$output_file"
    echo "-------------------------" >> "$output_file"
  else
    echo "Error: $markdown_file is not a valid file."
  fi
done

# Execute Django commands to update or create posts and delete missing posts
echo "$django_commands" | python3 manage.py shell

echo "Processing complete. Details stored in $output_file."
  