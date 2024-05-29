from django.db import models

# Create your models here.

class Soup(models.Model):
    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    temperature = models.CharField(max_length=100)
    broth = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} - {self.id}'