from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User

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
    
    def totale_mi_piace(self):
        return self.mi_piace.count()    
    
    #aggiungo queste due righe che servono a visualizzare sul database il titolo dell'articolo
    def __str__(self):
        return self.titolo

   
# modello che gestisce gli account del sito nel database
class AccountSubscriber(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    data_iscrizione = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Account"

    def __str__(self):
        return self.email
    
    def set_password(self, raw_password):
        #crea una password criptata
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        #verifica se la password corrisponde a quella salvata
        return check_password(raw_password, self.password)

class MiPiace(models.Model):
    utente = models.ForeignKey(User, on_delete=models.CASCADE)
    articolo = models.ForeignKey(Articolo, on_delete=models.CASCADE, related_name="mi_piace")

    class Meta:
        unique_together = ('utente', 'articolo')

    def __str__(self):
        return f"{self.utente.username} ha messo mi piace a {self.articolo.titolo}"