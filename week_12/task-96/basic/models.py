from django.db import models

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    ingredients = models.CharField(max_length=200)
    instructions = models.CharField(max_length=200)