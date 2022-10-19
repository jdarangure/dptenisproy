from django.db import models

# Create your models here.

class distributor(models.Model):
    id_dist = models.CharField(primary_key=True, max_length=25)
    fecha = models.DateTimeField()

    def __str__(self):
      restxt = "id: {0} (fecha: {1})"
      return restxt.format(self.id_dist, self.fecha)

class persons(models.Model):
    id_dist = models.CharField(max_length=25)
    nombre = models.CharField(max_length=25)
    apellido_paterno = models.CharField(max_length=25)
    apellido_materno = models.CharField(max_length=25)

    def __str__(self):
        restxt = "id: {0} Nombre Completo: {1} {2} {3}"
        return restxt.format(self.id_dist, self.nombre, self.apellido_paterno, self.apellido_materno)

class addresses(models.Model):
    id_dist = models.CharField(max_length=25)
    calle = models.CharField(max_length=25)
    numero_casa = models.PositiveIntegerField()
    colonia = models.CharField(max_length=25)

class phone_numbers(models.Model):
    id_dist = models.CharField(max_length=25)
    numero_telefono = models.PositiveBigIntegerField()
    activo = models.BooleanField()