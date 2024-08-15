from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CoordenadaForm
# Create your views here.

def loginPage(request):

    return render(request,"account/login.html")

@login_required(redirect_field_name='account_login')
def mainPage(request):

    return render(request,"pages/main.html")

def registerPage(request):

    return render(request,"account/signup.html")

def areaProprietario(request):
    if request.method == 'POST':
        form = CoordenadaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('coordenada_sucesso')
    else:
        form = CoordenadaForm()

    return render(request,"pages/alugarcamp.html", {'form': form})