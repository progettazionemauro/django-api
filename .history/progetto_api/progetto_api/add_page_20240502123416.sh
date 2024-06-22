#!/bin/bash

# Define paths
posts_dir="../sgb_start/content/posts
"
template_file="./../cheatsheet.md"  # Adjust this path to the location of your cheatsheet.md file

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

# Define the new file name
new_post_file="$posts_dir/il_mio_secondo_post.md"

# Check if the new post file already exists
if [ -f "$new_post_file" ]; then
  echo "Error: il_mio_secondo_post.md already exists!"
  exit 1
fi

# Get the front matter from the first post file
front_matter=$(grep -E '^\+\+\+' "$posts_dir/il_mio_primo_post.md")

# Append the content of the template file to the new post file
echo "$front_matter" > "$new_post_file"
cat "$template_file" >> "$new_post_file"

echo "New post created successfully: $new_post_file"
