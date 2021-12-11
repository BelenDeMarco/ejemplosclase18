from django.db import models

# Create your models here.
# en django siempre la clase hereda del paquete models la clase Model

class Curso (models.Model):

#genero atributo y tipo de datos con Field
    nombre= models.CharField(max_length=40)

    comision= models.IntegerField()

class Jugador (models.Model):

    apellido = models.CharField (max_length= 40)
    numero = models.IntegerField ()
    esBueno = models.BooleanField ()
    