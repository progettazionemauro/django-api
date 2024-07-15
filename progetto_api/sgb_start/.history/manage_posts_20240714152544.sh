#!/bin/bash

# Directory containing the posts
POSTS_DIR="/home/mauro/Scrivania/dJANGO_apI/progetto_api/sgb_start/content/posts"

# Check if the posts directory exists
if [ ! -d "$POSTS_DIR" ]; then
  echo "Directory $POSTS_DIR does not exist."
  exit 1
fi

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
