# Find Django PID and send SIGTERM signal
django_pid=$(pidof python) && kill "$django_pid" && echo "Django process terminated"

# Find Hugo PID and send SIGTERM signal
hugo_pid=$(pidof hugo) && kill "$hugo_pid" && echo "Hugo process terminated"
ps aux | grep "python manage.py runserver"; reset

