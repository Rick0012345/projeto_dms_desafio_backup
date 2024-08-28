from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CoordenadaForm, ReservasForm, UpdateUserForm, UpdateProfileForm
from .models import Coordenada, Profile
import json
# Create your views here.

def loginPage(request):

    return render(request,"account/login.html")

@login_required(redirect_field_name='account_login')
def mainPage(request):
    global reservas
    query = Coordenada.objects.all()  
    coordenadas = []
    for i in query:
        coordenadas.append({"latitude": i.latitude, "longitude": i.longitude})
    
    reservas = 0
    if request.method == 'POST':
        form = ReservasForm(request.POST)
        if form.is_valid():
            form.save()
            reservas += 1
            return redirect('main')
    return render(request,"pages/main.html", {'coordenadas': json.dumps(coordenadas), 'form': ReservasForm()})

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

# @login_required(redirect_field_name='account_login')
def profile(request):
    if request.method == 'POST':
        profile = Profile.objects.get(user=request.user)
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=profile)
        print(request.user) 
        print(profile)
        if user_form.is_valid() and profile_form.is_valid():
            print(profile_form.cleaned_data)
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='perfilUsuario')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)
    
    return render(request,"pages/profile.html",{'user_form': user_form, 'profile_form': profile_form})

def listacampos(request):
    return render(request,"pages/listcampos.html")


