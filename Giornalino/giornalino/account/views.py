from django.shortcuts import render, redirect
from .models import Account
import articoli.views


def registrati(request):
    if request.method == "POST":
        email = request.POST.get("email")  # 1
        password = request.POST.get("password")  # 2
        print(email, password)
        all_email = (
            Account.objects.all()
        )  # restituisce tutti(.all()) gli oggetti(.objects) presenti nella classe Account che sono stati salvati quindi nel db
        print(all_email)
        if len(all_email) > 0:
            for a in all_email:
                if (
                    a.email != email
                ):  # a.email è necessaria in modo tale che si vada a prendere l'attributo email dell'oggetto (a) che a sua volta viene assegnato tramite il for dalla funzione presente nella variabile all'email
                    account = Account(email=email, password=password, like=[{}])
                    print(
                        1
                    )  # stiamo passando i nostri valori 1 e 2 nella classe Account presente nel modello(vedi gli import)
                    account.save()
                    return render(request, "login.html")
        else:
            account = Account(email=email, password=password, like=[{}])
            # stiamo passando i nostri valori 1 e 2 nella classe Account presente nel modello(vedi gli import)
            account.save()
            return render(request, "login.html")
        return render(request, "registrati.html")
    else:
        return render(request, "registrati.html")


def login(request):
    if request.method == "POST":
        email = request.POST.get("email")  # 1
        password = request.POST.get("password")  # 2
        all_email = Account.objects.all()
        print(all_email)
        if len(all_email) > 0:
            for account in all_email:
                if account.email == email and account.password == password:
                    request.session["email"] = (
                        email  # si crea la sessione (request.session) e ad email(['email']) viene associata la variabile email, attraverso la quale si vuole fare il login
                    )
                    return redirect(articoli.views.home)
        else:
            print()
            if account.email == email and account.password == password:
                request.session["email"] = (
                    email  # si crea la sessione (request.session) e ad email(['email']) viene associata la variabile email, attraverso la quale si vuole fare il login
                )
                return redirect(articoli.views.home)
    return render(request, "login.html")


def logout(request):

    if "email" in request.session:
        del request.session[
            "email"
        ]  # si rimuove l'email in request.session['email'] facendo così il logout
    return render(request, "login.html")
