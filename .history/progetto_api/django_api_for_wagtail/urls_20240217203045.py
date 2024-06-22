from django.urls import path
from .views import NationAPIView

urlpatterns = [
    path('custom-api-viewer/', TemplateView.as_view(template_name='custom_api_viewer.html'), name='custom-api-viewer'),
]
    path('nations/', NationAPIView.as_view(), name='nation-api'),
    # Add more URL patterns as needed
]
