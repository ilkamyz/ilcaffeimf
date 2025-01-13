from django.shortcuts import render
from .models import Articolo

def lista_articoli(request):
    articoli = Articolo.objects.all().order_by('-data_pubblicazione')
    return render(request, 'lista_articoli.html', {'articoli': articoli})
