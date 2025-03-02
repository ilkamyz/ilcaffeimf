from django.urls import path, include
from . import views


urlpatterns = [
    path('registrati/', views.register, name='Registrati'),
    path('login/', views.login, name="Accedi"),
]
