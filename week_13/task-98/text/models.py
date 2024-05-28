from django.db import models


class Text(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField()