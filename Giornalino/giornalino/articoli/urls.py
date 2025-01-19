from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.lista_articoli, name='lista_articoli'),
    path('<int:pk>/', views.dettaglio_articolo, name='dettaglio_articolo'),
    path('mi-piace/<int:pk>/', views.toggle_mi_piace, name='toggle_mi_piace'),
]
