#!/bin/bash

# Function to handle Django model creation and migration
create_model_and_migrate() {
  echo "Enter the name of the new model (table):"
  read model_name

  # Ensure a valid number is entered for the number of fields
  while true; do
    echo "Enter the number of fields:"
    read num_fields
    if [[ $num_fields =~ ^[0-9]+$ ]]; then
      break
    else
      echo "Please enter a valid number for the fields."
    fi
  done

  # Create a temporary file to hold the new model
  new_model_file="new_model.py"

  # Start writing the model to the file
  echo "from django.db import models" > $new_model_file
  echo "" >> $new_model_file
  echo "class $model_name(models.Model):" >> $new_model_file

  # Array to store field names
  field_names=()

  # Loop to get the fields from the user
  for ((i=1; i<=num_fields; i++))
  do
    echo "Enter the field name for field $i:"
    read field_name
    field_names+=($field_name)  # Add field name to array

    echo "Choose the field type for $field_name (CharField, IntegerField, DateField):"
    read field_type

    # Add the field definition to the model
    if [ "$field_type" == "CharField" ]; then
      echo "    $field_name = models.CharField(max_length=255)" >> $new_model_file
    elif [ "$field_type" == "IntegerField" ]; then
      echo "    $field_name = models.IntegerField()" >> $new_model_file
    elif [ "$field_type" == "DateField" ]; then
      echo "    $field_name = models.DateField()" >> $new_model_file
    else
      echo "Invalid field type entered."
      exit 1
    fi
  done

  # Display available field names for the __str__ method
  echo "Choose the field to be used in the __str__ method from the following: ${field_names[*]}"
  read str_field

  # Check if the selected field is valid
  if [[ ! " ${field_names[@]} " =~ " ${str_field} " ]]; then
    echo "Invalid field selected for __str__ method."
    exit 1
  fi

  # Finish the model with a __str__ method
  echo "" >> $new_model_file
  echo "    def __str__(self):" >> $new_model_file
  echo "        return self.$str_field" >> $new_model_file

  # Append the newly created model into the Django app models.py file
  cat $new_model_file >> /home/mauro/Scrivania/dJANGO_apI/progetto_api/blog/models.py

  # Remove the temporary model file
  rm $new_model_file

  # Run makemigrations and migrate commands
  python3 manage.py makemigrations blog
  python3 manage.py migrate blog
}

# Ensure all processes are stopped before restarting
echo "Checking and killing processes using port 8000..."
pids=$(lsof -ti :8000)

if [ -n "$pids" ]; then
  echo "Port 8000 is in use by the following processes: $pids"
  kill -9 $pids
  echo "Processes killed."
else
  echo "Port 8000 is not in use."
fi

# Call the function to create the model and run migrations
create_model_and_migrate

# Start the Django server
echo "Starting Django server..."
python3 manage.py runserver &

# Optionally start the Hugo server
echo "Starting Hugo server..."
cd ./sgb_start/
hugo server -D
