#!/bin/bash

# Check if any process is listening on port 8000
pids=$(lsof -ti :8000)

if [ -n "$pids" ]; then
    echo "Port 8000 is in use by the following processes: $pids"

    # Kill all processes using port 8000
    echo "Killing processes with PIDs: $pids"
    kill -9 $pids

    echo "Processes killed."
else
    echo "Port 8000 is not in use."
fi

# Check if Celery is running and kill it if necessary
celery_pids=$(pgrep -f 'celery')

if [ -n "$celery_pids" ]; then
    echo "Celery is running with the following PIDs: $celery_pids"

    # Kill the Celery processes
    echo "Killing Celery processes with PIDs: $celery_pids"
    kill -9 $celery_pids

    echo "Celery processes killed."
else
    echo "Celery is not running."
fi

# Start Django server
python3 manage.py runserver &

# Start Celery worker
celery -A progetto_api worker --loglevel=info &

# Start Hugo server
cd ./sgb_start/
hugo server -D
