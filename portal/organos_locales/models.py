from django.db import models

class Organization(models.Model):
    nombre = models.CharField(max_length=200)
    siglas = models.CharField(max_length=200)
    domicilio = models.CharField(max_length=200)
    codigo_postal = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)
    provincia = models.CharField(max_length=200)
    prefijo = models.IntegerField()
    telefonos = models.CharField(max_length=200)
    fax = models.CharField(max_length=200, null=True)
    correo_electronico = models.CharField(max_length=200, null=True) 
    director = models.CharField(max_length=200)
    director2 = models.CharField(max_length=200, null=True)