from operator import mod
from os import link
from django.db import models

class Dulce(models.Model):
    nombre = models.CharField(max_length= 250)
    tipo = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nombre


