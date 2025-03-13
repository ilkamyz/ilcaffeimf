from django.db import models


# modello che gestisce gli account del sito nel databaseclass Account(models.Model):
class Account(models.Model):
    email = models.EmailField(unique=True)
    password = models.TextField()
    like = models.JSONField(default=list)

    def __str__(self):
        return f"{self.email}"
