from django.db import models

class Articolo(models.Model):
    titolo = models.CharField(max_length=200)
    contenuto = models.TextField()
    autore = models.CharField(max_length=100)
    data_pubblicazione = models.DateTimeField(auto_now_add=True)
    #aggiungo queste due righe che servono a visualizzare su databasd il titolo direttamente
    def __str__(self):
        return self.titolo


