from django.db import models
from django.contrib.auth.hashers import make_password, check_password

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
