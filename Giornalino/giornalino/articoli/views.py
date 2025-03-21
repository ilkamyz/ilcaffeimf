from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import Articolo
from account.models import Account
import account.views


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

    elif ordinamento == "autore":
        autori=[]
        articoli2=[]
        for articolo in articoli:
            if articolo.autore not in autori:
                autori.append(articolo.autore)
            else:
                pass

        for articolo in articoli:
            a=autori.index(articolo.autore)
            articoli2.insert(a, articolo)

        articoli=articoli2

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


def autore_dettaglio(request, author_name):
    articoli = Articolo.objects.filter(autore=author_name)
    return render(
        request,
        "autore_dettaglio.html",
        {"author_name": author_name, "articoli": articoli},
    )


def home(request):
    if "email" in request.session:
        articoli = Articolo.objects.all()
        a = True
        request.session["previous_page"] = request.path
        return render(request, "home.html", {"articoli": articoli, "autenticato": a})

    else:
        articoli = Articolo.objects.all()
        request.session["previous_page"] = request.path
        return render(request, "home.html", {"articoli": articoli})


def like(request, pk):
    if "email" in request.session:
        account = get_object_or_404(Account, email=request.session["email"])
        if str(pk) in account.like[0].keys():
            if (
                account.like[0][str(pk)] == True
            ):  # se esiste pk nella mia sessione posso mettere like, (CORREGGERE!) idea: ad ogni articolo che si crea aggiungo ad una ista o dizionao i vari valori booleani

                articolo = get_object_or_404(Articolo, pk=pk)
                articolo.like = articolo.like + 1
                articolo.save()
                account.like[0][str(pk)] = False
                account.save()
                print(account.like)
                return redirect(f"/{pk}/")
            else:
                articolo = get_object_or_404(Articolo, pk=pk)
                account.like[0][str(pk)] = True
                account.save()
                articolo.like = articolo.like - 1
                articolo.save()
                return redirect(f"/{pk}/")

        else:
            account.like[0][f"{pk}"] = False
            account.save()
            articolo = get_object_or_404(Articolo, pk=pk)
            articolo.like = articolo.like + 1
            articolo.save()
            return redirect(f"/{pk}/")
    else:
        return redirect(f"/{pk}/")
