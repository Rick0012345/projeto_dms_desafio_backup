from django import forms
from .models import Coordenada , Reservas

class CoordenadaForm(forms.ModelForm):
    class Meta:
        model = Coordenada
        fields = ['latitude', 'longitude']
class ReservasForm(forms.ModelForm):
    class Meta:
        model = Reservas
        fields = ['dia', 'inicio', 'final']