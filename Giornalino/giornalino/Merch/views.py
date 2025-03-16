from django.shortcuts import render, get_object_or_404
from .models import Merch

# Create your views here.
def merch(request):
    merch=Merch.objects.all()
    numero=len(merch)
    return render(request, 'merch.html', {'merch': merch, 'numero':numero})

def dettaglio_prodotto(request, pk):
    prodotto= get_object_or_404(Merch, pk=pk)
    return render(request, 'prodotto.html', {'prodotto':prodotto})