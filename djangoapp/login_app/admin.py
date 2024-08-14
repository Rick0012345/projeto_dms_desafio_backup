from django.contrib import admin
from login_app.models import Campo

# Register your models here.
@admin.register(Campo)
class AddressAdmin(admin.ModelAdmin):
    pass