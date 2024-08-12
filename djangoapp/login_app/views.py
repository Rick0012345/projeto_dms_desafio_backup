from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

def loginPage(request):

    return render(request,"account/login.html")

@login_required(redirect_field_name='account_login')
def mainPage(request):

    return render(request,"pages/main.html")

def registerPage(request):

    return render(request,"account/signup.html")

def areaProprietario(requests):
    return render(requests,"pages/alugarcamp.html")