from django.db import models

# Create your models here.

class Dictionary(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=200)
    def __str__(self):
        return self.title