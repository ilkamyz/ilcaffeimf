from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail
from newsletter.models import IscrizioneNewsletter
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Articolo(models.Model):
    titolo = models.CharField(max_length=200)
    id = models.AutoField(primary_key=True)
    contenuto = RichTextUploadingField()
    descrizione_breve = RichTextUploadingField()
    autore = models.CharField(max_length=100)
    data_pubblicazione = models.DateTimeField(auto_now_add=True)
    immagine = models.ImageField(upload_to="articoli/", blank=True, null=True)
    like = models.IntegerField(default=0)

    # serve a ordinare gli articoli nel database in base alla data di pubblicazione
    class Meta:
        verbose_name = "Articolo"
        verbose_name_plural = "Articoli"
        ordering = ["-data_pubblicazione"]

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        iscritti = IscrizioneNewsletter.objects.filter(is_active=True)

        super().save(*args, **kwargs)
        if is_new:
            for iscritto in iscritti:
                send_mail(
                    subject=f"Nuovo articolo disponibile!!!",
                    message=f"""
    Ciao,

    Abbiamo appena aggiunto un nuovo articolo</a> al nostro sito! Puoi visualizzarlo cliccando sul seguente link:

    https://ilcaffe.pythonanywhere.com/{self.id}/

    Grazie per seguirci!
    """,
                    from_email="ilcaffemajoranafascitelli@gmail.com",
                    recipient_list=[iscritto.email],
                    fail_silently=False,
                    html_message=f"""
    Ciao,

    Abbiamo appena aggiunto un nuovo <a href="https://ilcaffe.pythonanywhere.com/{self.id}/">articolo</a> al nostro sito! 



    Grazie per seguirci!
    """,
                )

    # aggiungo queste due righe che servono a visualizzare sul database il titolo dell'articolo
    def __str__(self):
        return self.titolo
