from django.db import models

class Coop(models.Model):
    name = models.CharField(max_length=200)

class Partnet(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    coop = models.ForeignKey(Coop)
