from django.db import models

# Create your models here.
# en django siempre la clase hereda del paquete models la clase Model

class Curso (models.Model):

#genero atributo y tipo de datos con Field
    nombre= models.CharField(max_length=40)

    comision= models.IntegerField()

#modifica la forma de ver los datos incluso en el panel de admin de Django
    def __str__ (self):

        return f"CURSO: {self.nombre} COMISION {self.comision}"


class Jugador (models.Model):

    apellido = models.CharField (max_length= 40)
    numero = models.IntegerField ()
    