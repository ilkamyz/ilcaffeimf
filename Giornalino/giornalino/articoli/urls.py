from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_articoli, name='lista_articoli'),
]
