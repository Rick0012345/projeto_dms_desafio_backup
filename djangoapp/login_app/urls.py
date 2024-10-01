from django.urls import path, include
from login_app.views import (
    mainPage,
    registerPage,
    areaProprietario,
    profile,
    listacampos,
    fazer_relatorio,
    feedPage
)

urlpatterns = [
    path("accounts/profile/", mainPage, name="main"),
    path("signup/", registerPage, name="signup"),
    path("accounts/profile/add-campo", areaProprietario, name="alugar-campo"),
    path("accounts/profile/perfilUsuario", profile, name="perfilUsuario"),
    path("accounts/profile/listas", listacampos, name="listacampos"),
    path("accounts/profile/relatorio", fazer_relatorio, name="relatorio"),
    path("accounts/profile/feedback/<int:id>",feedPage,name="feedback"),
    path('campo/<int:id>/feedback/', feedPage, name='feedPage'),
]
