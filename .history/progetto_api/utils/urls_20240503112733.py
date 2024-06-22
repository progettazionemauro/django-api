from django.urls import path
from . import views

urlpatterns = [
    path('run-script/', views.run_script_view, name='run_script'),
    # Define other URL patterns as needed
]
