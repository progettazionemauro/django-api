from django.urls import path
from .views import NationAPIView

urlpatterns = [
    path('nations/', NationAPIView.as_view(), name='nation-api'),
    # Add more URL patterns as needed
]