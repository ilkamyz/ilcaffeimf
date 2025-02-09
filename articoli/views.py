from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import Articolo, MiPiace


def lista_articoli(request):
    # Recupera il valore selezionato dall'utente
    ordinamento = request.POST.get(
        "ordinamento", "recenti"
    )  # Valore di default: 'recenti'
    articoli = Articolo.objects.all().order_by("-data_pubblicazione")

    if ordinamento == "recenti":
        articoli = articoli.order_by("-data_pubblicazione")

    elif ordinamento == "meno_recenti":
        articoli = articoli.order_by("data_pubblicazione")

    request.session["previous_page"] = request.path

    return render(request, "lista_articoli.html", {"articoli": articoli})


def dettaglio_articolo(request, pk):
    articolo = get_object_or_404(Articolo, pk=pk)
    previous_page = request.session.get("previous_page", "/articoli/")

    return render(
        request,
        "dettaglio_articolo.html",
        {"articolo": articolo, "previous_page": previous_page},
    )


def toggle_mi_piace(request, pk):
    if request.method == "POST":
        articolo = get_object_or_404(Articolo, pk=pk)
        mi_piace, creato = MiPiace.objects.get_or_create(
            utente=request.user, articolo=articolo
        )

        if not creato:
            mi_piace.delete()
            stato = "rimosso"
        else:
            stato = "aggiunto"

        return JsonResponse({"stato": stato, "totale": articolo.totale_mi_piace()})

    return JsonResponse({"errore": "Metodo non supportato"}, status=405)


def autore_dettaglio(request, author_name):
    articoli = Articolo.objects.filter(autore=author_name)
    return render(
        request,
        "autore_dettaglio.html",
        {"author_name": author_name, "articoli": articoli},
    )


def home(request):
    articoli = Articolo.objects.all()
    request.session["previous_page"] = request.path
    return render(request, "home.html", {"articoli": articoli})
