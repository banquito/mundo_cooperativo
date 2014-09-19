from django.db import models

# Create your models here.
class Province(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Organization(models.Model):
    province = models.ForeignKey(Province)
    name = models.CharField(max_length=200)
    siglas = models.CharField(max_length=200)
    domicilio = models.CharField(max_length=200)
    codigo_postal = models.IntegerField()
    ciudad = models.CharField(max_length=200)
    prefijo = models.IntegerField()
    telefonos = models.IntegerField()
    fax = models.IntegerField()
    correo_electronico = models.CharField(max_length=200) 
    director = models.CharField(max_length=200)
    director2 = models.CharField(max_length=200)