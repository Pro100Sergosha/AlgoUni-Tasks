from django.db import models


# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    date_created = models.DateField(auto_now_add=True)