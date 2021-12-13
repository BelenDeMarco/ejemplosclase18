from django.shortcuts import render

from django.http import HttpResponse

from AppCoder.models import Jugador

# Create your views here.
# Primer vista

def inicio (request):

    # return HttpResponse ("Esto es una prueba del inicio")

    return render(request, 'AppCoder/inicio.html')

def jugadores (request):

    return render (request,'AppCoder/jugadores.html' )

def jugadoresFormulario (request):

    if request.method == "POST":

        jugadorInsta = Jugador(apellido = request.POST["apellido"], numero = request.POST["numero"])

        jugadorInsta.save()

        return render (request,'AppCoder/Inicio.html' )

    return render (request,'AppCoder/jugadoresFormulario.html' )

