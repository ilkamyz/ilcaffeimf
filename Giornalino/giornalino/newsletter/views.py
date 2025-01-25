from django.shortcuts import render, redirect
from django.contrib import messages
from .models import IscrizioneNewsletter
from .forms import NewsletterForm
from django.core.mail import send_mail
from django.conf import settings

def iscrizione_newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Iscrizione completata con successo!")
            except IntegrityError:
                messages.error(request, "Questa email è già registrata.")
            return redirect('lista_articoli')  # Modifica '#' con la tua vista principale
    else:
        form = NewsletterForm()
    return render(request, 'iscrizione.html', {'form': form})



def invia_newsletter(request):
    iscritti = IscrizioneNewsletter.objects.filter(is_active=True)
    destinatari = [iscritto.email for iscritto in iscritti]

    oggetto = "La nostra ultima newsletter!"
    messaggio = messaggio = "Grazie per seguirci! Ecco le ultime novità. Per disiscriverti, clicca qui: http://tuodominio.com/newsletter/disiscrizione/{email}/"

    mittente = settings.EMAIL_HOST_USER

    send_mail(oggetto, messaggio, mittente, destinatari)
    return render(request, 'inviata.html', {})

def disiscrizione_newsletter(request, email):
    try:
        iscrizione = IscrizioneNewsletter.objects.get(email=email)
        iscrizione.is_active = False
        iscrizione.save()
        messages.success(request, "Ti sei disiscritto con successo.")
    except IscrizioneNewsletter.DoesNotExist:
        messages.error(request, "Email non trovata.")
    return redirect('#')  # Modifica '#' con la tua vista principale
