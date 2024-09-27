from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Coordenada(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    valor_hora = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        verbose_name = "Coordenada"
        verbose_name_plural = "Coordenadas"

    def __str__(self):
        return str(f"Latitude :{self.latitude} | Longitude: {self.longitude}")


class DadosCampo(models.Model):
    #adicionar nome do campo
    endereco = models.CharField(max_length=150)
    telefone = models.CharField(max_length=11)       # TROCAR PARA CHARFIELD DEPOIS
    email = models.EmailField()
    foto = models.ImageField( default= "default.jpg",upload_to="camp_pics")

    def save(self, *args, **kwargs):
        super().save()
    
    class Meta:
        verbose_name = "DadosCampo"
        verbose_name_plural = "DadosCampos"



    


class Reserva(models.Model):
    from django import forms

    dia = models.DateField()
    inicio = models.TimeField()
    final = models.TimeField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"

    def __str__(self):
        return str(f"dia :{self.dia} | inicio: {self.inicio} | final: {self.final}")
    

    def clean(self):
       
        overlapping = Reserva.objects.filter(
                    # football_field=self.football_field,
                    dia=self.dia,
                    inicio__lt=self.final,
                    final__gt=self.inicio,
                    # status="confirmed",
                ).exclude(pk=self.pk)
        
        if overlapping.exists():
            raise ValidationError(
                _("This time slot overlaps with an existing reservation.")
            )  



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(default="default.jpg", upload_to="profile_pics")

    def save(self, *args, **kwargs):
        super().save()



class Feedback(models.Model):
    campoAvaliado = models.ForeignKey(DadosCampo,related_name="avaliacoes",on_delete=models.CASCADE)
    nomeUsuario = models.ForeignKey(Profile,related_name="usuario",on_delete=models.CASCADE)
    comentario = models.TextField()

    estrelas = [
        (1,"1 Estrela"),
        (2,"2 Estrelas"),
        (3,"3 Estrelas"),
        (4,"4 Estrelas"),
        (5,"5 Estrelas")
    ]

    avaliacoes = models.PositiveSmallIntegerField(default=1, choices=estrelas)