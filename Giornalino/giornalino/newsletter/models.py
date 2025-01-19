from django.db import models

class IscrizioneNewsletter(models.Model):
    email = models.EmailField(unique=True)
    data_iscrizione = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email
