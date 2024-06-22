#!/bin/bash

# Directory containing markdown files
markdown_dir="/home/mauro/Scrivania/dJANGO_apI/progetto_api/sgb_start/content/posts/"

# Check if the directory exists
if [ ! -d "$markdown_dir" ]; then
  echo "Error: Directory $markdown_dir does not exist."
  exit 1
fi

# Iterate over all markdown files in the directory
for markdown_file in "$markdown_dir"/*.md; do
  if [ -f "$markdown_file" ]; then
    # Read contents of the markdown file
    content=$(cat "$markdown_file")

    # Extract title from filename
    filename=$(basename -- "$markdown_file")
    title="${filename%.*}"

    # Construct image_link based on the extracted title
    image_link="http://localhost:1313/posts/${title}/"

    # Print the details (in real usage, you might want to save these details to a database)
    echo "Title: $title"
    echo "File Name: $filename"
    echo "Content: $content"
    echo "Image Link: $image_link"
    echo "-------------------------"

    # If you had to save it to a database, you would place the database insertion logic here.
    # This is a placeholder for demonstration purposes.
  else
    echo "Error: $markdown_file is not a valid file."
  fi
done
