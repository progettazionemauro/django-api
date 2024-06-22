#!/bin/bash
progetto_api/run_project.sh

# Navigate to the Django project directory and run the server
# cd /progetto_api
python3 manage.py runserver &

# Navigate to the Hugo project directory and run the server
cd ./sgb_start/
hugo server -D
