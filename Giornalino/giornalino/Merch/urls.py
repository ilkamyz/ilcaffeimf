from django.urls import path, include
from . import views


urlpatterns = [
    path("merch/", views.merch, name="merch"),
    path("merch/<int:pk>/", views.dettaglio_prodotto, name="merch_id"),

]
