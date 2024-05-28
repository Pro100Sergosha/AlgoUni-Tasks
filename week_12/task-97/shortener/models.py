from django.db import models

# Create your models here.
class Url(models.Model):
    long_url = models.URLField()
    short_url = models.CharField(max_length=200)
    redirections = models.IntegerField(default=0)