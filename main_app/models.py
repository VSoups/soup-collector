from django.db import models
from django.urls import reverse

# Create your models here.

class Soup(models.Model):
    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    temperature = models.CharField(max_length=100)
    broth = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} - {self.id}'
    
    # must be named 'get_absolute_url'?
    def get_absolute_url(self):
        # 'reverse' allows the use of the url template from urls.py
        return reverse('detail', kwargs={'soup_id': self.id})