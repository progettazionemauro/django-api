from django.db import models
from django.utils.text import slugify
from django.utils import timezone

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

    def save(self, *args, **kwargs):
        if not self.file_name:
            self.file_name = slugify(self.title).replace('-', '_') + '.md'
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
class maglia(models.Model):
    tessuto = models.CharField(max_length=255)

    def __str__(self):
        return self.tessuto
from django.db import models

class piante_grasse(models.Model):
    specie = models.CharField(max_length=255)
    sottospecie = models.CharField(max_length=255)

    def __str__(self):
        return self.specie
