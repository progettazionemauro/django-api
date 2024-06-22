from django.db import models

# Create your models here. Mauro
class CustomFeature(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    file_name = models.CharField(max_length=255, unique=True)  # Name of the file
    image_name = models.CharField(max_length=255)  # Name of the image
    image_link = models.URLField()  # Link to the image

    def __str__(self):
        return self.title