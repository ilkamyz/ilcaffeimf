from django.shortcuts import render, redirect
from django.contrib import messages
from .models import AccountSubscriber
from newsletter.models import IscrizioneNewsletter

def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        subscribe_to_newsletter = request.POST.get('newsletter') == 'on'

        if password != confirm_password:
            messages.error(request, 'Le password non coincidono.')
            return render(request, 'Registrati.html')

        if AccountSubscriber.objects.filter(email=email).exists():
            messages.error(request, 'Email già registrata.')
            return render(request, 'Registrati.html')

        # Crea l'account con la password criptata
        account = AccountSubscriber(email=email)
        account.set_password(password)
        account.save()

        # Iscrivi l'utente alla newsletter, se selezionato
        if subscribe_to_newsletter:
            IscrizioneNewsletter.objects.get_or_create(email=email)

        messages.success(request, 'Account creato con successo!')
        return redirect('login')  # Modifica con l'URL della pagina di login

    return render(request, 'Registrati.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if password != AccountSubscriber.password:
            messages.error(request, 'Password errata.')
            return render(request, 'accedi.html')

        if AccountSubscriber.objects.filter(email!=email).exists():
            messages.error(request, 'Email errata.')
            return render(request, 'accedi.html')

        messages.success(request, 'Bentornato!')
        return redirect('') 

    return render(request, 'accedi.html')
