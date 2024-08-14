from django.db import models

# Create your models here.

class Campo(models.Model):
    def registrar_campo(self):
        pass
    latitude = models.FloatField()
    longitude = models.FloatField()
    class Meta:
        verbose_name = 'Campo'
        verbose_name_plural = 'Campos'
    def __str__(self):
        return str(f"Latitude :{self.latitude} | Longitude: {self.longitude}")