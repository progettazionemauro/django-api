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

class piante_grasse(models.Model):
    specie = models.CharField(max_length=255)
    sottospecie = models.CharField(max_length=255)

    def __str__(self):
        return self.specie

class piante(models.Model):
    specie = models.CharField(max_length=255)
    famiglia = models.CharField(max_length=255)

    def __str__(self):
        return self.specie
from django.db import models

class piantegrasse(models.Model):
    specie = models.CharField(max_length=255)

    def __str__(self):
        return self.specie
from django.db import models

class animali(models.Model):
    famiglia = models.CharField(max_length=255)

    def __str__(self):
        return self.famiglia
from django.db import models

class mari(models.Model):
    tipi = models.CharField(max_length=255)

    def __str__(self):
        return self.tipi
from django.db import models

class auto(models.Model):
    tipo = models.CharField(max_length=255)

    def __str__(self):
        return self.tipo
from django.db import models

class camion(models.Model):
    tipo = models.CharField(max_length=255)

    def __str__(self):
        return self.tipo
from django.db import models

class birre(models.Model):
    marche = models.CharField(max_length=255)

    def __str__(self):
        return self.marche
from django.db import models

class bibite(models.Model):
    marca = models.CharField(max_length=255)

    def __str__(self):
        return self.marca
from django.db import models

class profumi(models.Model):
    marca = models.CharField(max_length=255)

    def __str__(self):
        return self.marca
from django.db import models

class citta(models.Model):
    nazione = models.CharField(max_length=255)

    def __str__(self):
        return self.nazione
from django.db import models

class ringhiere(models.Model):
    tipologia = models.CharField(max_length=255)
    marca = models.CharField(max_length=255)

    def __str__(self):
        return self.marca
