from django.contrib import admin
from login_app.models import Coordenada, Reservas

# Register your models here.
@admin.register(Coordenada)
class AddressAdmin(admin.ModelAdmin):
    pass
@admin.register(Reservas)
class AdressAdmin(admin.ModelAdmin):
    pass