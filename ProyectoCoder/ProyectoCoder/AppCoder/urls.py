from django.urls import path

from AppCoder import views

urlpatterns = [

    path ('Inicio', views.inicio, name = "Inicio"),

    path ('Jugadores', views.jugadores, name = "Jugadores"),
    
    path ('jugadoresFormulario', views.jugadoresFormulario, name = "JugadoresFormulario")
    

]