from django.db import models
from django.urls import reverse

class Python(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    morph = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'python_id': self.id})
