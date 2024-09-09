from django.contrib import admin
from login_app.models import Coordenada, Reserva
from .models import Profile


# Register your models here.
@admin.register(Coordenada)
class AddressAdmin(admin.ModelAdmin):
    pass


@admin.register(Reserva)
class AdressAdmin(admin.ModelAdmin):
    pass


admin.site.register(Profile)
