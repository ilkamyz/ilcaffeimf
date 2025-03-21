from django.db import models

# Create your models here.
class Merch(models.Model):
    nome = models.CharField(max_length=200, blank=True, null=True)
    id = models.AutoField(primary_key=True)
    descrizione = models.CharField(max_length=200, blank=True, null=True)
    prezzo=models.CharField(max_length=200, blank=True, null=True)
    image1 = models.ImageField(upload_to="Merch/", blank=True, null=True)
    image2 = models.ImageField(upload_to="Merch/", blank=True, null=True)
    image3 = models.ImageField(upload_to="Merch/", blank=True, null=True)

    def __str__(self):
        return f'{self.nome}'