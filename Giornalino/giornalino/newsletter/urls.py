from django.urls import path
from . import views

urlpatterns = [
    path('', views.iscrizione_newsletter, name='iscrizione_newsletter'),
]
