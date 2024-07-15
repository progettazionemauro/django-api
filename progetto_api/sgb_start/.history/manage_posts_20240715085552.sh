#!/bin/bash

# Directory containing the posts
POSTS_DIR="/home/mauro/Scrivania/dJANGO_apI/progetto_api/sgb_start/content/posts"

# Check if the posts directory exists
if [ ! -d "$POSTS_DIR" ]; then
  echo "Directory $POSTS_DIR does not exist."
  exit 1
fi

# Function to create a new post
create_post() {
  read -p "Enter the title of the new post: " title
  read -p "Enter the date (YYYY-MM-DDTHH:MM:SS+TZ): " date
  read -p "Enter tags (comma separated): " tags
  read -p "Enter categories (comma separated): " categories
  read -p "Enter cover image path: " cover_image
  read -p "Enter cover image alt text: " cover_alt
  read -p "Enter cover image caption: " cover_caption

  # Set default values if no input is provided
  title=${title:-"Default Title"}
  date=${date:-$(date +"%Y-%m-%dT%H:%M:%S%z" | sed 's/\(..\)$/:\1/')}
  tags=${tags:-"default,tag"}
  categories=${categories:-"default,category"}
  cover_image=${cover_image:-"img/default.png"}
  cover_alt=${cover_alt:-"Default Alt Text"}
  cover_caption=${cover_caption:-"Default Caption"}

  filename=$(echo "$title" | tr ' ' '_' | tr '[:upper:]' '[:lower:]').md
  filepath="$POSTS_DIR/$filename"

  # Create the new post with the specified or default values
  cat <<EOF > "$filepath"
+++
title = "$title"
date = "$date"
draft = true
tags = [$(echo $tags | sed 's/,/, /g')]
categories = [$(echo $categories | sed 's/,/, /g')]
[cover]
    image = "$cover_image"
    alt = "$cover_alt"
    caption = "$cover_caption"
+++
EOF

  echo "New post '$title' has been created at $filepath."
}

# List all posts
echo "List of posts:"
ls "$POSTS_DIR"

# Ask for the post to delete
read -p "Enter the name of the post to delete: " POST_NAME

# Check if the post exists
if [ -f "$POSTS_DIR/$POST_NAME" ]; then
  # Delete the post
  rm "$POSTS_DIR/$POST_NAME"
  echo "Post '$POST_NAME' has been deleted."
else
  echo "Post '$POST_NAME' does not exist."
fi

# Ask if user wants to create a new post
read -p "Do you want to create a new post? (y/n): " CREATE_NEW

if [ "$CREATE_NEW" == "y" ]; then
  create_post
fi
