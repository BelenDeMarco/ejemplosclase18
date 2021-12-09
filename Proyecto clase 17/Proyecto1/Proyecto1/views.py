from django.http import HttpResponse

from  datetime import datetime

from django.template import Template, Context

from django.template import loader

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

    mejorEstudiante = "Mariano"

    nota = 8.9

    fecha = datetime.now

    estudiantesSimpaticos = ["Juan", "Pepe", "Lore"]

    dicc = {"nombre": mejorEstudiante , "nota": nota, "fecha":fecha, "estudiantes": estudiantesSimpaticos}

    plantilla = loader.get_template ("template1.html")

    documento = plantilla.render(dicc)

    # miHTML = open ("C:/Users/Belu/Desktop/Clase 18/ejemplosclase18/Proyecto clase 17/Proyecto1/Proyecto1/plantillas/template1.html")

    # plantilla = Template(miHTML.read())

    # miHTML.close ()

    # miContexto = Context (dicc)

    # documento = plantilla.render (miContexto)

    return HttpResponse (documento)

    




