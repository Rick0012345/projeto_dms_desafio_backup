from django import forms
from .models import Coordenada, Reserva, Profile, DadosCampo, Feedback
from datetime import datetime
from django.contrib.auth.models import User


class CoordenadaForm(forms.ModelForm):
    class Meta:
        model = Coordenada
        fields = ["latitude", "longitude", "valor_hora"]


class DadosCampoForm(forms.ModelForm):
    class Meta:
        model = DadosCampo
        fields = ["endereco","telefone","email","foto","nome"]
           

class ReservasForm(forms.ModelForm):
    dia = forms.DateField(widget=forms.SelectDateWidget())
    inicio = forms.TimeField(widget=forms.TimeInput(attrs={"type": "time"}))
    final = forms.TimeField(widget=forms.TimeInput(attrs={"type": "time"}))

    class Meta:
        model = Reserva
        fields = ["dia", "inicio", "final"]


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    email = forms.EmailField(
        required=True, widget=forms.TextInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = User
        fields = ["username", "email"]


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["img"]

class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = ["nomeUsuario","comentario","avaliacoes"]