from django.db import models

# Create your models here.
# la clase hereda del paquete models

class Curso (models.Model):

#genero atributo y tipo de datos con Field
    nombre= models.CharField(max_length=40)

    comision= models.IntegerField()


