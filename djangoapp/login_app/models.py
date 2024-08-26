from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
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
    from django import forms
    dia = models.DateField()
    inicio = models.TimeField()
    final = models.TimeField()

    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'

    def __str__(self):
        return str(f"dia :{self.dia} | inicio: {self.inicio} | final: {self.final}")


class CadastroUsuario(models.Model):
    User = get_user_model()
    User.objects.all()

class ImgUser(models.Model):
    imagem = models.ImageField(upload_to='images/')

   
   