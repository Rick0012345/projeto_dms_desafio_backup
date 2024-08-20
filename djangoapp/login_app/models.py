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
    
    class Reservas:
        dia = models.DateTimeField(_("Dia"), auto_now=False, auto_now_add=False)
        inicio = models.DateTimeField(_("hora_inicio"), auto_now=False, auto_now_add=False)
        final = models.DateTimeField(_("hora_final"), auto_now=False, auto_now_add=False)
    
   
   