from django.contrib import admin
from login_app.models import Coordenada

# Register your models here.
@admin.register(Coordenada)
class AddressAdmin(admin.ModelAdmin):
    pass