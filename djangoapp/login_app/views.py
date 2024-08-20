from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CoordenadaForm
from .models import Coordenada
import json
# Create your views here.

def loginPage(request):

    return render(request,"account/login.html")

@login_required(redirect_field_name='account_login')
def mainPage(request):
    query = Coordenada.objects.all()  
    coordenadas = []
    for i in query:
        coordenadas.append({"latitude": i.latitude, "longitude": i.longitude})
    
    return render(request,"pages/main.html", {'coordenadas': json.dumps(coordenadas)})

def registerPage(request):

    return render(request,"account/signup.html")

def areaProprietario(request):
    query = Coordenada.objects.all()  
    coordenadas = []
    for i in query:
        coordenadas.append({"latitude": i.latitude, "longitude": i.longitude})

    if request.method == 'POST':
        form = CoordenadaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alugar-campo')
    else:
        form = CoordenadaForm()


    return render(request,"pages/alugarcamp.html", {'form': form, 'coordenadas': json.dumps(coordenadas)})