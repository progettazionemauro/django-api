#!/bin/bash

echo "Enter the name of the new model (table):"
read model_name

echo "Enter the number of fields:"
read num_fields

# Create a temporary file to hold the new model
new_model_file="new_model.py"

# Start writing the model to the file
echo "from django.db import models" > $new_model_file
echo "" >> $new_model_file
echo "class $model_name(models.Model):" >> $new_model_file

# Loop to get the fields from the user
for ((i=1; i<=num_fields; i++))
do
  echo "Enter the field name for field $i:"
  read field_name

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
  fi
done

# Ask for the field to use in the __str__ method
echo "Choose the field to be used in the __str__ method from the following:"
field_options=$(awk '/models./ {print $1}' $new_model_file | tail -n +2)
echo $field_options
read str_field

# Finish the model with a __str__ method
echo "" >> $new_model_file
echo "    def __str__(self):" >> $new_model_file
echo "        return self.$str_field" >> $new_model_file

# Move the newly created model into the Django app models.py file
cat $new_model_file >> /home/mauro/Scrivania/dJANGO_apI/progetto_api/blog/models.py

# Remove the temporary model file
rm $new_model_file

# Apply migrations
python3 manage.py makemigrations
python3 manage.py migrate

# Start the Django project
python3 manage.py runserver &

# Optionally start the Hugo server
cd ./sgb_start/
hugo server -D