from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import JsonResponse
from .forms import NewsletterSubscriptionForm
from .models import Articolo, NewsletterSubscriber, MiPiace

def lista_articoli(request):
    articoli = Articolo.objects.all().order_by('-data_pubblicazione')
    return render(request, 'lista_articoli.html', {'articoli': articoli})

def dettaglio_articolo(request, pk):
    articolo = get_object_or_404(Articolo, pk=pk)
    return render(request, 'dettaglio_articolo.html', {'articolo': articolo})

# view del form di iscrizione
def iscrizione_newsletter(request):
    if request.method == 'POST':
        form = NewsletterSubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Iscrizione completata! Grazie per esserti iscritto alla nostra newsletter.")
            return redirect('') 
        else:
            messages.error(request, "C'è stato un problema con l'iscrizione. Per favore riprova.")
    else:
        form = NewsletterSubscriptionForm()

    return render(request, 'iscrizione_newsletter.html', {'form': form})

def toggle_mi_piace(request, pk):
    if request.method == 'POST':
        articolo = get_object_or_404(Articolo, pk=pk)
        mi_piace, creato = MiPiace.objects.get_or_create(utente=request.user, articolo=articolo)

        if not creato:
            mi_piace.delete()
            stato = 'rimosso'
        else:
            stato = 'aggiunto'

        return JsonResponse({'stato': stato, 'totale': articolo.totale_mi_piace()})

    return JsonResponse({'errore': 'Metodo non supportato'}, status=405)    