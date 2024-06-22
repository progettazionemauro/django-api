#!/bin/bash

# Check if any process is listening on port 8000
if netstat -tuln | grep ':8000 ' >/dev/null 2>&1; then
    echo "Port 8000 is in use."

    # Get the PID of the process using port 8000
    pid=$(netstat -tuln | grep ':8000 ' | awk '{print $7}' | cut -d'/' -f1)

    # Kill the process
    echo "Killing process with PID $pid"
    kill -9 "$pid"

    echo "Process killed."
else
    echo "Port 8000 is not in use."
fi

# Navigate to the Django project directory and run the server
# cd /progetto_api
python3 manage.py runserver &

# Navigate to the Hugo project directory and run the server
cd ./sgb_start/
hugo server -D
