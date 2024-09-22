#!/bin/bash

create_model_and_migrate() {
  echo "Enter the name of the new model (table):"
  read model_name

  # Validate model name
  if [[ ! $model_name =~ ^[a-zA-Z_][a-zA-Z0-9_]*$ ]]; then
    echo "Invalid model name. Please use letters, numbers, and underscores."
    exit 1
  fi

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

  new_model_file="new_model.py"
  echo "from django.db import models" > $new_model_file
  echo "" >> $new_model_file
  echo "class $model_name(models.Model):" >> $new_model_file

  field_names=()
  for ((i=1; i<=num_fields; i++))
  do
    echo "Enter the field name for field $i:"
    read field_name
    field_names+=($field_name)

    echo "Choose the field type for $field_name (CharField, IntegerField, DateField):"
    read field_type

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

  echo "Choose the field to be used in the __str__ method from the following: ${field_names[*]}"
  read str_field

  if [[ ! " ${field_names[@]} " =~ " ${str_field} " ]]; then
    echo "Invalid field selected for __str__ method."
    exit 1
  fi

  echo "" >> $new_model_file
  echo "    def __str__(self):" >> $new_model_file
  echo "        return self.$str_field" >> $new_model_file

  cat $new_model_file >> /home/mauro/Scrivania/dJANGO_apI/progetto_api/blog/models.py
  rm $new_model_file

  python3 manage.py makemigrations blog
  python3 manage.py migrate blog
}

create_model_and_migrate

pids=$(lsof -ti :8000)

if [ -n "$pids" ]; then
  kill -9 $pids
fi

python3 manage.py runserver &
cd ./sgb_start/
hugo server -D
