#!/bin/bash

# Define paths
# posts_dir="../sgb_start/content/posts"
posts_dir="/home/mauro/Scrivania/dJANGO_apI/progetto_api/sgb_start/content/posts"
# template_file="./../cheatsheet.md"  # Adjust this path to the location of your cheatsheet.md file
template_file="/home/mauro/Scrivania/dJANGO_apI/progetto_api/cheatsheet.md"

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

# Find the latest post number
latest_post=$(ls -1 "$posts_dir" | grep -E "^post_number_[0-9]+\.md$" | sort -r | head -n 1)
if [ -z "$latest_post" ]; then
  latest_post_number=1
else
  latest_post_number=$(echo "$latest_post" | grep -oE "[0-9]+" | sed 's/^0*//')
  latest_post_number=$((latest_post_number + 1))
fi

# Define the new file name
new_post_file="$posts_dir/post_number_${latest_post_number}.md"

# Check if the new post file already exists
if [ -f "$new_post_file" ]; then
  echo "Error: $new_post_file already exists!"
  exit 1
fi

# Extract front matter using sed from the first post
front_matter=$(sed -n '/^\+\+\+/,/^\+\+\+/p' "$posts_dir/post_number_1.md")

# Check if front matter is empty
if [ -z "$front_matter" ]; then
    echo "Error: Front matter not found in the first post"
    exit 1
fi

# Append the front matter to the new post file
echo "$front_matter" > "$new_post_file"

# Append the content of the template file to the new post file
cat "$template_file" >> "$new_post_file"
echo "New post created successfully: $new_post_file"

# Call the function to read files in the posts directory
read_files "$posts_dir"