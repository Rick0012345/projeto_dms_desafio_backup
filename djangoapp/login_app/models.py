from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Coordenada(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    class Meta:
        verbose_name = 'Coordenada'
        verbose_name_plural = 'Coordenadas'
        
    def __str__(self):
        return str(f"Latitude :{self.latitude} | Longitude: {self.longitude}")
    
class Reservas(models.Model):
    dia = models.DateField(_("Dia"), auto_now = True, auto_now_add=True)
    inicio = models.TimeField(_("inicio"), auto_now = True, auto_now_add=True)
    final = models.TimeField(_("final"), auto_now = True, auto_now_add=True)

    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'

    def __str__(self):
        return str(f"dia :{self.dia} | inicio: {self.inicio} | final: {self.final}")

   
   