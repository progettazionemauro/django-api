#!/bin/bash

# Log file for debugging
LOG_FILE="/home/mauro/Scrivania/dJANGO_apI/progetto_api/sgb_start/manage_posts.log"
echo "Script called with action: $1" >> "$LOG_FILE"

# Directory containing the posts
POSTS_DIR="/home/mauro/Scrivania/dJANGO_apI/progetto_api/sgb_start/content/posts"
echo "Posts directory: $POSTS_DIR" >> "$LOG_FILE"

# Check if the posts directory exists
if [ ! -d "$POSTS_DIR" ]; then
  echo "Directory $POSTS_DIR does not exist." >> "$LOG_FILE"
  exit 1
fi

# Function to create a new post
create_post() {
  POST_NAME="$1.md"
  POST_TITLE="$2"
  POST_DATE="$3"
  POST_TAGS="$4"
  POST_CATEGORIES="$5"
  POST_IMAGE="$6"
  POST_IMAGE_ALT="$7"
  POST_IMAGE_CAPTION="$8"

  echo "Creating post with name: $POST_NAME" >> "$LOG_FILE"
  echo "Image link: $POST_IMAGE" >> "$LOG_FILE"

  # Set default values if no input is provided
  POST_TITLE=${POST_TITLE:-"Default Title"}
  POST_DATE=${POST_DATE:-$(date +"%Y-%m-%dT%H:%M:%S%:z")}
  POST_TAGS=${POST_TAGS:-"adventure,foodie,travel,fitness,nature,fun,inspiration"}
  POST_CATEGORIES=${POST_CATEGORIES:-"adventure,food,health,art,entertainment,science,lifestyle"}
  POST_IMAGE=${POST_IMAGE:-"img/default.jpeg"}
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

  echo "Post '$POST_NAME' has been created at $POST_FILE." >> "$LOG_FILE"
}

# Function to delete a post
delete_post() {
  POST_NAME="$1.md"
  echo "Deleting post with name: $POST_NAME" >> "$LOG_FILE"
  if [ -f "$POSTS_DIR/$POST_NAME" ]; then
    rm "$POSTS_DIR/$POST_NAME"
    echo "Post '$POST_NAME' has been deleted." >> "$LOG_FILE"
  else
    echo "Post '$POST_NAME' does not exist." >> "$LOG_FILE"
  fi
}

# Main script logic
ACTION="$1"
shift

case "$ACTION" in
  add)
    create_post "$@"
    ;;
  delete)
    delete_post "$1"
    ;;
  *)
    echo "Invalid action. Use 'add' or 'delete'." >> "$LOG_FILE"
    exit 1
    ;;
esac
