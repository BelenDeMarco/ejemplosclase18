from django.urls import path

from AppCoder import views

urlpatterns = [

    path ('Inicio', views.inicio),

    path ('Jugadores', views.jugadores),
    


]