from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm,  UserEditForm
from django.contrib.auth.decorators import login_required
from users.models import Profile


def login_request(request):

    msg_login = ""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                return render(request, "AppLitobar/daddy.html")

        msg_login = "Usuario o contraseña incorrectos"

    form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form, "msg_login": msg_login})



def register(request):
    msg_register = ""
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "AppLitobar/daddy.html")
        msg_register = "Error en los datos ingresados"
    else:
        form = UserRegisterForm()
    
    if 'usable_password' in form.fields:
        del form.fields['usable_password']

    return render(request, "users/registro.html", {"form": form, "msg_register": msg_register})



@login_required
def editar_perfil(request):
    usuario = request.user

    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST, request.FILES, instance=usuario.profile)
        if miFormulario.is_valid():
            miFormulario.save()
            return redirect('Profile')
    else:
        miFormulario = UserEditForm(instance=usuario.profile)

    return render(request, "users/editar_usuario.html", {"mi_form": miFormulario, "usuario": usuario})


@login_required
def profile(request):
    usuario = request.user
    perfil = usuario.profile  
    return render(request, "users/profile.html", {"usuario": usuario, "perfil": perfil})