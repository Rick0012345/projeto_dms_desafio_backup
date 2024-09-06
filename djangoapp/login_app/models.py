from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.
class Coordenada(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    valor_hora = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    class Meta:
        verbose_name = 'Coordenada'
        verbose_name_plural = 'Coordenadas'

    # def save(self, *args, **kwargs):
    #     super().save()
        
    def __str__(self):
        return str(f"Latitude :{self.latitude} | Longitude: {self.longitude}")
    
class Reservas(models.Model):
    from django import forms
    
    dia = models.DateField()
    inicio = models.TimeField()
    final = models.TimeField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'

    def __str__(self):
        return str(f"dia :{self.dia} | inicio: {self.inicio} | final: {self.final}")

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def save(self, *args, **kwargs):
        super().save()


    



    
    

   
   