from django.urls import path, include
from . import views


urlpatterns = [
    path("login/", views.login, name="login"),
    path("registrati/", views.registrati, name="registrati"),
    path("logout/", views.logout, name="logout"),
]
