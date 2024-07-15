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
  read -p "Enter the name of the new post (with .md extension): " POST_NAME
  read -p "Enter the title of the new post: " POST_TITLE
  read -p "Enter the date of the new post (YYYY-MM-DDTHH:MM:SS+TZ): " POST_DATE
  read -p "Enter the tags for the new post (comma separated): " POST_TAGS
  read -p "Enter the categories for the new post (comma separated): " POST_CATEGORIES
  read -p "Enter the image path for the new post: " POST_IMAGE
  read -p "Enter the image alt text: " POST_IMAGE_ALT
  read -p "Enter the image caption: " POST_IMAGE_CAPTION

  # Set default values if no input is provided
  POST_TITLE=${POST_TITLE:-"Default Title"}
  POST_DATE=${POST_DATE:-$(date +"%Y-%m-%dT%H:%M:%S%:z")}
  POST_TAGS=${POST_TAGS:-"adventure,foodie,travel,fitness,nature,fun,inspiration"}
  POST_CATEGORIES=${POST_CATEGORIES:-"adventure,food,health,art,entertainment,science,lifestyle"}
  POST_IMAGE=${POST_IMAGE:-"img/default.png"}
  POST_IMAGE_ALT=${POST_IMAGE_ALT:-"Default Alt Text"}
  POST_IMAGE_CAPTION=${POST_IMAGE_CAPTION:-"Default Caption"}

  # Format tags and categories for TOML
  formatted_tags=$(echo "$POST_TAGS" | sed 's/ *, */", "/g' | sed 's/^/["/' | sed 's/$/"]/')
  formatted_categories=$(echo "$POST_CATEGORIES" | sed 's/ *, */", "/g' | sed 's/^/["/' | sed 's/$/"]/')

  # Create the new post file
  POST_FILE="$POSTS_DIR/$POST_NAME"
  cat <<EOF > "$POST_FILE"
+++
title = "$POST_TITLE"
date = "$POST_DATE"
draft = true
ShowToc = true
tags = $formatted_tags
categories = $formatted_categories
[cover]
    image = "$POST_IMAGE"
    alt = "$POST_IMAGE_ALT"
    caption = "$POST_IMAGE_CAPTION"
+++
EOF

  echo "Post '$POST_NAME' has been created."
}

# List all posts
echo "List of posts:"
ls "$POSTS_DIR"

# Ask the user for the action they want to perform
echo "Choose an action:"
echo "1) Delete a post"
echo "2) Add a new post"
read -p "Enter the number of the action you want to perform: " ACTION

# Function to delete a post
delete_post() {
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
}

# Perform the chosen action
case $ACTION in
  1)
    delete_post
    ;;
  2)
    create_post
    ;;
  *)
    echo "Invalid action."
    ;;
esac
