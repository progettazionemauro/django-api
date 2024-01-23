from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("django_api_for_wagtail/", include('django_api_for_wagtail.urls')),
]
