from django.urls import path, include
from login_app.views import mainPage,registerPage,areaProprietario,profile
urlpatterns = [
    path("accounts/profile/",mainPage,name="main"),
    path("signup/", registerPage, name="signup"),
    path("accounts/profile/add-campo",areaProprietario,name="alugar-campo"),
    path("accounts/profile/perfilUsuario",profile,name="perfilUsuario"),
]

