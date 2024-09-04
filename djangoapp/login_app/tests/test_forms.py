import pytest
from django.contrib.auth.models import User
from login_app.forms import CoordenadaForm, ReservasForm, UpdateUserForm, UpdateProfileForm
from login_app.models import Profile

@pytest.mark.django_db
def test_coordenada_form_valid_data():
    form_data = {
        'latitude': 12.345678,
        'longitude': 98.765432,
    }
    form = CoordenadaForm(data=form_data)
    assert form.is_valid()
    assert form.cleaned_data['latitude'] == 12.345678
    assert form.cleaned_data['longitude'] == 98.765432


@pytest.mark.django_db
def test_coordenada_form_invalid_data():
    form_data = {
        'latitude': 'invalid',
        'longitude': 'invalid',
    }
    form = CoordenadaForm(data=form_data)
    assert not form.is_valid()
    assert 'latitude' in form.errors
    assert 'longitude' in form.errors

@pytest.mark.django_db
def test_reservas_form_valid_data():
    form_data = {
        'dia': '2024-09-03',
        'inicio': '10:00',
        'final': '12:00',
    }
    form = ReservasForm(data=form_data)
    assert form.is_valid()
    assert form.cleaned_data['dia'] == '2024-09-03'
    assert form.cleaned_data['inicio'] == '10:00'
    assert form.cleaned_data['final'] == '12:00'


@pytest.mark.django_db
def test_update_user_form_valid_data():
    user = User.objects.create_user(username='testuser', password='testpass', email='test@example.com')
    form_data = {
        'username': 'newusername',
        'email': 'newemail@example.com',
    }
    form = UpdateUserForm(instance=user, data=form_data)
    assert form.is_valid()
    updated_user = form.save()
    assert updated_user.username == 'newusername'
    assert updated_user.email == 'newemail@example.com'


@pytest.mark.django_db
def test_update_profile_form_valid_data():
    user = User.objects.create_user(username='testuser', password='testpass', email='test@example.com')
    # Cria o perfil apenas se não existir
    profile,created = Profile.objects.get_or_create(user=user)  # Apenas para garantir que o perfil exista
    # Prepara os dados para o formulário
    form_data = {
        'img': None,  # Aqui você pode adicionar uma imagem válida se necessário
    }
    form = UpdateProfileForm(instance=profile, data=form_data)
    
    # Verifica se o formulário é válido
    assert form.is_valid()
    # Salva o perfil atualizado
    updated_profile = form.save()
    # Verifica se a imagem foi atualizada (ou permanece None)
    assert updated_profile.img == form_data['img']

