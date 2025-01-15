from django.db import models

class Articolo(models.Model):
    titolo = models.CharField(max_length=200)
    id = models.AutoField(primary_key=True)
    contenuto = models.TextField()
    autore = models.CharField(max_length=100)
    data_pubblicazione = models.DateTimeField(auto_now_add=True)

    #serve a ordinare gli articoli nel database in base alla data di pubblicazione
    class Meta:
        ordering = ['-data_pubblicazione']
        
    #aggiungo queste due righe che servono a visualizzare sul database il titolo dell'articolo
    def __str__(self):
        return self.titolo


