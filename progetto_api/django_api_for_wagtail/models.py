from django.db import models

class Nation(models.Model):
    name = models.CharField(max_length=255, unique=True)
    capital = models.CharField(max_length=255)

    def __str__(self):
        return self.name

