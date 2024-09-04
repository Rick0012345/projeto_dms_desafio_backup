from django import forms
from .models import Coordenada , Reservas, Profile
from datetime import datetime
from django.contrib.auth.models import User
class CoordenadaForm(forms.ModelForm):
    class Meta:
        model = Coordenada
        fields = ['latitude', 'longitude']
class ReservasForm(forms.ModelForm):
    dia = forms.DateField(widget=forms.SelectDateWidget())
    inicio = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    final = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    valor_total = forms.DecimalField(label='Valor Total', required=True, disabled=True)

    class Meta:
        model = Reservas
        fields = ['dia', 'inicio', 'final', 'valor_total']

    def clean(self):
        cleaned_data = super().clean()
        inicio = cleaned_data.get('inicio')
        final = cleaned_data.get('final')

        if inicio and final:
            # Calcular a duração
            inicio_dt = datetime.combine(cleaned_data.get('dia'), inicio)
            final_dt = datetime.combine(cleaned_data.get('dia'), final)

            if final_dt <= inicio_dt:
                raise forms.ValidationError("O horário final deve ser depois do horário de início.")

            # Calcular a duração em horas
            duracao = final_dt - inicio_dt
            duracao_em_horas = duracao.total_seconds() / 3600  # Converte para horas

            # Calcular o valor total (exemplo: R$ 50 por hora)
            valor_por_hora = 50
            valor_total = duracao_em_horas * valor_por_hora

            # Atribui o valor total ao campo
            cleaned_data['valor_total'] = valor_total

        return cleaned_data
    # chamar a função clean no meu models

class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['img']
        