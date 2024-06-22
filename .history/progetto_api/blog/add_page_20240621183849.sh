#!/bin/bash

# Enable debug mode
set -x

# Define paths
posts_dir="/home/mauro/Scrivania/dJANGO_apI/progetto_api/sgb_start/content/posts"
template_file="/home/mauro/Scrivania/dJANGO_apI/progetto_api/cheatsheet.md"

# Function to read all files in a directory
read_files() {
    local directory="$1"
    local file_count=0
    for file in "$directory"/*; do
        if [ -f "$file" ]; then
            echo "Found file: $file"
            ((file_count++))
        fi
    done
    echo "Total files found: $file_count"
}

# Find the latest post number
latest_post_number=1
while [ -f "$posts_dir/post_number_${latest_post_number}.md" ]; do
  latest_post_number=$((latest_post_number + 1))
done

# Define the new file name
new_post_file="$posts_dir/post_number_${latest_post_number}.md"

# Check if the posts directory exists
if [ ! -d "$posts_dir" ]; then
  echo "Error: Hugo posts directory not found!"
  exit 1
fi

# Check if the template file exists
if [ ! -f "$template_file" ]; then
  echo "Error: Template file not found!"
  exit 1
fi

# Append the content of the template file to the new post file
cat "$template_file" > "$new_post_file"
echo "New post created successfully: $new_post_file"

# Verify the new post file was created
if [ ! -f "$new_post_file" ]; then
  echo "Error: Failed to create new post file!"
  exit 1
fi

# Call the function to read files in the posts directory
read_files "$posts_dir"

# Introduce a small delay to ensure the file is accessible
sleep 1

# Optional: Trigger Hugo to rebuild the site
hugo -s /home/mauro/Scrivania/dJANGO_apI/progetto_api/sgb_start

# Disable debug mode
set +x
