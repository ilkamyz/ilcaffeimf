from django.shortcuts import render, get_object_or_404
from .models import Articolo

def lista_articoli(request):
    articoli = Articolo.objects.all().order_by('-data_pubblicazione')
    return render(request, 'lista_articoli.html', {'articoli': articoli})

def dettaglio_articolo(request, pk):
    articolo = get_object_or_404(Articolo, pk=pk)
    return render(request, 'dettaglio_articolo.html', {'articolo': articolo})
