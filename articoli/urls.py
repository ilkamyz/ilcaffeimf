from django.urls import path, include
from . import views


urlpatterns = [
    path("articoli/", views.lista_articoli, name="lista_articoli"),
    path("<int:pk>/", views.dettaglio_articolo, name="dettaglio_articolo"),
    path("autore/<str:author_name>/", views.autore_dettaglio, name="autore_dettaglio"),
    path("", views.home, name="home"),
    path("like/<int:pk>/", views.like, name="like"),
]
