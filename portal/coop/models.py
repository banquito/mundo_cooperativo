from django.db import models
from django.contrib.auth.models import AbstractUser

class Coop(models.Model):
    name = models.CharField(max_length=200)

class Partner(AbstractUser):
    coop = models.ForeignKey(Coop)
