from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CoordenadaForm, ReservasForm, UpdateUserForm, UpdateProfileForm
from .models import Coordenada, Profile, Reserva
import json
from datetime import datetime
from decimal import Decimal


def loginPage(request):
    return render(request, "account/login.html")


@login_required(redirect_field_name="account_login")
def mainPage(request):
    global reservas
    query = Coordenada.objects.all()
    coordenadas = []

    for i in query:
        coordenadas.append({"latitude": i.latitude, "longitude": i.longitude})

    reservas = 0
    if request.method == "POST":
        ini = datetime.strptime(request.POST.get("inicio"), "%H:%M")
        fin = datetime.strptime(request.POST.get("final"), "%H:%M")

        if fin <= ini:
            messages.error(
                request, "O horário de início deve ser antes do horário de final"
            )
        duracao = fin - ini
        duracao_em_horas = duracao.total_seconds() / 3600
        valor_por_hora = (
            50  # ALTERAR PARA QUE PEGUE O VALOR DO CAMPO ESPECÍFICO POR HORA
        )
        valor_total = duracao_em_horas * valor_por_hora

        instancia = Reserva(
            valor_total=valor_total
        )  # depois trocar para o singular (RESERVA)

        form = ReservasForm(data=request.POST, instance=instancia)

        print(request.POST)
        if form.is_valid():
            form.save()
            reservas += 1
            messages.success(request, "Reservado com sucesso")
            return redirect("main")

        else:
            print(form.errors)
            messages.error(request, "Erro ao reservar campo")

    context = {"coordenadas": json.dumps(coordenadas), "form": ReservasForm()}
    return render(request, "pages/main.html", context)


def registerPage(request):

    return render(request, "account/signup.html")


def areaProprietario(request):
    query = Coordenada.objects.all()
    coordenadas = []
    for i in query:
        coordenadas.append({"latitude": i.latitude, "longitude": i.longitude})
    if request.method == "POST":
        form = CoordenadaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("alugar-campo")
    else:
        form = CoordenadaForm()
    context = {"form": form, "coordenadas": json.dumps(coordenadas)}
    return render(request, "pages/alugarcamp.html", context)


@login_required(redirect_field_name="account_login")
def profile(request):
    if request.method == "POST":
        profile = Profile.objects.get(user=request.user)
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=profile)
        print(request.user)
        print(profile)
        if user_form.is_valid() and profile_form.is_valid():
            print(profile_form.cleaned_data)
            user_form.save()
            profile_form.save()
            messages.success(request, "Your profile is updated successfully")
            return redirect(to="perfilUsuario")
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(
        request,
        "pages/profile.html",
        {"user_form": user_form, "profile_form": profile_form},
    )


def listacampos(request):
    return render(request, "pages/listcampos.html")

@login_required
def fazer_relatorio(request):
    # Buscar todas as reservas
    reservas = Reserva.objects.all().order_by('dia', 'inicio')
    # Calcular o total de todas as reservas
    total_valor = Decimal('0.00')
    for reserva in reservas:
        try:
            total_valor += Decimal(str(reserva.valor_total))
        except Exception as e:
            print(f"Error processing reserva {reserva.id}: {e}")
            print(f"valor_total: {reserva.valor_total}, type: {type(reserva.valor_total)}")
    
    context = {
        'reservas': reservas,
        'total_valor': total_valor,
    }
    
    return render(request, "pages/relatorio.html", context)