from django.urls import path
from . import views

urlpatterns = [
    path('newsletter/', views.iscrizione_newsletter, name='iscrizione_newsletter'),
]
