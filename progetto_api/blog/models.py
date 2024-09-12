from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from django_api_for_wagtail.models import Nation

class Post(models.Model):
    title = models.CharField(max_length=255)
    file_name = models.CharField(max_length=255, unique=True, editable=False)
    date = models.DateTimeField(default=timezone.now)
    tags = models.CharField(max_length=255, default="adventure,foodie,travel,fitness,nature,fun,inspiration")
    categories = models.CharField(max_length=255, default="adventure,food,health,art,entertainment,science,lifestyle")
    image_name = models.CharField(max_length=255)
    image_alt = models.CharField(max_length=255, default="Default Alt Text")
    image_caption = models.CharField(max_length=255, default="Default Caption")
    image_link = models.URLField()
    draft = models.BooleanField(default=True)
    nation = models.ForeignKey(Nation, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.file_name:
            self.file_name = slugify(self.title).replace('-', '_') + '.md'
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


# Nuovo modello per gestire la configurazione delle tabelle dinamiche
class TableConfiguration(models.Model):
    table_name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.table_name


class FieldConfiguration(models.Model):
    table = models.ForeignKey(TableConfiguration, related_name='fields', on_delete=models.CASCADE)
    field_name = models.CharField(max_length=255)
    field_type = models.CharField(max_length=50, choices=[
        ('CharField', 'Stringa'),
        ('IntegerField', 'Numero Intero'),
        ('DateField', 'Data'),
    ])

    def __str__(self):
        return f"{self.field_name} ({self.get_field_type_display()})"
