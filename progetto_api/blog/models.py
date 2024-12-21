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


class AdditionalImage(models.Model):
    post = models.ForeignKey(Post, related_name='additional_images', on_delete=models.CASCADE)
    image_name = models.CharField(max_length=255)
    image_alt = models.CharField(max_length=255, default="Default Alt Text")
    image_caption = models.CharField(max_length=255, default="Default Caption")
    image_link = models.URLField()

    def __str__(self):
        return f"{self.image_name} ({self.post.title})"


# Mantieni tutti gli altri modelli invariati
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


class animali(models.Model):
    famiglia = models.CharField(max_length=255)

    def __str__(self):
        return self.famiglia


class mari(models.Model):
    tipi = models.CharField(max_length=255)

    def __str__(self):
        return self.tipi


class auto(models.Model):
    tipo = models.CharField(max_length=255)

    def __str__(self):
        return self.tipo


class camion(models.Model):
    tipo = models.CharField(max_length=255)

    def __str__(self):
        return self.tipo


class birre(models.Model):
    marche = models.CharField(max_length=255)

    def __str__(self):
        return self.marche


class bibite(models.Model):
    marca = models.CharField(max_length=255)

    def __str__(self):
        return self.marca


class profumi(models.Model):
    marca = models.CharField(max_length=255)

    def __str__(self):
        return self.marca


class citta(models.Model):
    nazione = models.CharField(max_length=255)

    def __str__(self):
        return self.nazione


class ringhiere(models.Model):
    tipologia = models.CharField(max_length=255)
    marca = models.CharField(max_length=255)

    def __str__(self):
        return self.marca
