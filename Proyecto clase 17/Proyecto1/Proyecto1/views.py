from django.http import HttpResponse

from  datetime import datetime

from django.template import Template, Context

def saludo(request):
	return HttpResponse ("Hola Django - Coder")

def segundaVista (request):
    return HttpResponse ("No puedo creer que estoy haciendo esto")


def dia(request):
    
    variable = datetime.now ()

    return HttpResponse (f"El dia de hoy es {variable}")

def apellido (request,ape):

    return HttpResponse (f"El profe de coder {ape} es muy bueno")

def probandoTemplate (request):

    miHTML = open ("C:/Users/Belu/Desktop/Proyecto clase 17/Proyecto1/Proyecto1/plantillas/template1.html")

    plantilla = Template(miHTML.read())

    miHTML.close ()

    miContexto = Context ()

    documento = plantilla.render (miContexto)

    return HttpResponse (documento)

    




