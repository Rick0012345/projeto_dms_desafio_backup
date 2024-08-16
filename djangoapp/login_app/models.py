from django.db import models

# Create your models here.

class Coordenada(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    class Meta:
        verbose_name = 'Coordenada'
        verbose_name_plural = 'Coordenadas'
        
    def __str__(self):
        return str(f"Latitude :{self.latitude} | Longitude: {self.longitude}")
    
   
   