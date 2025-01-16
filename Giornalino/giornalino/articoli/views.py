from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import NewsletterSubscriptionForm
from .models import Articolo, NewsletterSubscriber

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