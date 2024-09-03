import pytest
from login_app.models import Coordenada
from django.core.files.uploadedfile import SimpleUploadedFile


@pytest.mark.django_db
def test___str__():
    coordenada = Coordenada(latitude=0.0, longitude=0.0)
    assert str(coordenada) == 'Latitude :0.0 | Longitude: 0.0'


