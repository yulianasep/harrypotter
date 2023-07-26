from django.db import models
from django.contrib.auth.models import AbstractUser

class User(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.nombre


class House(models.Model):
    name = models.CharField(max_length=50)
    mascot = models.CharField(max_length=50)
    head_of_house = models.CharField(max_length=50)
    house_ghost = models.CharField(max_length=50)
    founder = models.CharField(max_length=50)
    school = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    

class Spell(models.Model):
    spellName = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return f"{self.spellName}"