#!/bin/bash

# Directory containing the posts
POSTS_DIR="/home/mauro/Scrivania/dJANGO_apI/progetto_api/sgb_start/content/posts"

# Directory for default images
IMG_DIR="/home/mauro/Scrivania/dJANGO_apI/progetto_api/sgb_start/static/img"

# Ensure the image directory exists
if [ ! -d "$IMG_DIR" ]; then
  mkdir -p "$IMG_DIR"
fi

# Ensure default image exists
if [ ! -f "$IMG_DIR/default.jpeg" ]; then
  echo "default.png not found in $IMG_DIR. Please add the default image to continue."
  exit 1
fi

# Check if the posts directory exists
if [ ! -d "$POSTS_DIR" ]; then
  echo "Directory $POSTS_DIR does not exist."
  exit 1
fi

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

# Function to add a new post
add_post() {
  # Ask for the new post details
  read -p "Enter the name of the new post (with .md extension): " POST_NAME
  read -p "Enter the title of the new post: " POST_TITLE
  read -p "Enter the date of the new post (YYYY-MM-DDTHH:MM:SS+TZ): " POST_DATE
  read -p "Enter the image path for the new post: " POST_IMAGE
  read -p "Enter the image alt text: " POST_IMAGE_ALT
  read -p "Enter the image caption: " POST_IMAGE_CAPTION
  read -p "Enter the tags for the new post (comma separated): " POST_TAGS
  read -p "Enter the categories for the new post (comma separated): " POST_CATEGORIES
  read -p "Enter the content of the new post: " POST_CONTENT

  # Set default values if inputs are empty
  POST_TITLE=${POST_TITLE:-"Untitled Post"}
  POST_DATE=${POST_DATE:-$(date +"%Y-%m-%dT%H:%M:%S%z")}
  POST_IMAGE=${POST_IMAGE:-"img/default.png"}
  POST_IMAGE_ALT=${POST_IMAGE_ALT:-"Default Image"}
  POST_IMAGE_CAPTION=${POST_IMAGE_CAPTION:-"Default Caption"}
  POST_TAGS=${POST_TAGS:-"general"}
  POST_CATEGORIES=${POST_CATEGORIES:-"misc"}
  POST_CONTENT=${POST_CONTENT:-"This is a default content."}

  # Create the new post file
  POST_FILE="$POSTS_DIR/$POST_NAME"
  {
    echo "+++"
    echo "title = '$POST_TITLE'"
    echo "date = $POST_DATE"
    echo "draft = true"
    echo "ShowToc = true"
    echo "tags = [$(echo $POST_TAGS | sed 's/,/, /g')]"
    echo "categories = [$(echo $POST_CATEGORIES | sed 's/,/, /g')]"
    echo "[cover]"
    echo "    image= \"$POST_IMAGE\""
    echo "    alt= \"$POST_IMAGE_ALT\""
    echo "    caption= \"$POST_IMAGE_CAPTION\""
    echo "+++"
    echo ""
    echo "$POST_CONTENT"
  } > "$POST_FILE"

  echo "Post '$POST_NAME' has been created."
}

# Perform the chosen action
case $ACTION in
  1)
    delete_post
    ;;
  2)
    add_post
    ;;
  *)
    echo "Invalid action."
    ;;
esac
