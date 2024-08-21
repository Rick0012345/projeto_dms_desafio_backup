from django import forms
from .models import Coordenada , Reservas

class CoordenadaForm(forms.ModelForm):
    class Meta:
        model = Coordenada
        fields = ['latitude', 'longitude']
class ReservasForm(forms.ModelForm):
    # 
    dia = forms.DateField(widget = forms.SelectDateWidget())
    inicio = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    final = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    class Meta:
        model = Reservas
        fields = ['dia', 'inicio', 'final']

