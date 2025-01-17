from django.db import models

class Articolo(models.Model):
    titolo = models.CharField(max_length=200)
    id = models.AutoField(primary_key=True)
    contenuto = models.TextField()
    descrizione_breve = models.TextField(default='')
    autore = models.CharField(max_length=100)
    data_pubblicazione = models.DateTimeField(auto_now_add=True)

    #serve a ordinare gli articoli nel database in base alla data di pubblicazione
    class Meta:
        verbose_name = "Articolo"
        verbose_name_plural = "Articoli"
        ordering = ['-data_pubblicazione']
        
    #aggiungo queste due righe che servono a visualizzare sul database il titolo dell'articolo
    def __str__(self):
        return self.titolo

# aggiungo qui un modello per la newsletter molto basic
class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)  # Per gestire chi vuole annullare l'iscrizione
    date_subscribed = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Iscritto"
        verbose_name_plural = "Iscritti"

    def __str__(self):
        return self.email
    
# modello che gestisce gli account del sito nel database
class AcoountSubscriber(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=80)
    is_active = models.BooleanField(default=True)
    data_iscrizione = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Account"

    def __str__(self):
        return self.email
