from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=400)

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    favourite = models.ManyToManyField(User, related_name='favourite', blank=True)

    def __str__(self):
        return self.title
