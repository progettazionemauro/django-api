#!/bin/bash

# Directory containing markdown files
markdown_dir="/home/mauro/Scrivania/dJANGO_apI/progetto_api/sgb_start/content/posts/"

# Output file to store processed file details
output_file="/home/mauro/Scrivania/dJANGO_apI/progetto_api/s/processed_files.txt"

# Check if the directory exists
if [ ! -d "$markdown_dir" ]; then
  echo "Error: Directory $markdown_dir does not exist."
  exit 1
fi

# Create or clear the output file
> "$output_file"

# Iterate over all markdown files in the directory
for markdown_file in "$markdown_dir"/*.md; do
  if [ -f "$markdown_file" ]; then
    # Read contents of the markdown file
    content=$(cat "$markdown_file" | sed 's/"/\\"/g' | sed "s/'/\\'/g")

    # Extract title from filename
    filename=$(basename -- "$markdown_file")
    title="${filename%.*}"

    # Construct image_link based on the extracted title
    image_link="http://localhost:1313/posts/${title}/"

    # Print the details (for demonstration purposes)
    echo "Title: $title"
    echo "File Name: $filename"
    echo "Content: $content"
    echo "Image Link: $image_link"
    echo "-------------------------"

    # Save the data to the Django database using the Django shell
    echo "from blog.models import Post; Post.objects.create(title=\"$title\", text=\"$content\", file_name=\"$filename\", image_name='', image_link=\"$image_link\")" | python3 manage.py shell

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

echo "Processing complete. Details stored in $output_file."
