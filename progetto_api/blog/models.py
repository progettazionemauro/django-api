from django.db import models
from django.utils import timezone
from django_api_for_wagtail.models import Nation  # Import Nation model

class Post(models.Model):
    title = models.CharField(max_length=255)
    file_name = models.CharField(max_length=255, unique=True)
    date = models.DateTimeField(default=timezone.now)
    tags = models.CharField(max_length=255, default="adventure,foodie,travel,fitness,nature,fun,inspiration")
    categories = models.CharField(max_length=255, default="adventure,food,health,art,entertainment,science,lifestyle")
    image_name = models.CharField(max_length=255)
    image_alt = models.CharField(max_length=255, default="Default Alt Text")
    image_caption = models.CharField(max_length=255, default="Default Caption")
    image_link = models.URLField()
    draft = models.BooleanField(default=True)
    nation = models.ForeignKey(Nation, on_delete=models.CASCADE)  # Link to Nation model

    def __str__(self):
        return self.title
