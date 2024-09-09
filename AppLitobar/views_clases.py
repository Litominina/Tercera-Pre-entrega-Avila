from django.shortcuts import render
from .models import Cita 
from django.views.generic import ListView 
from django.views.generic.detail import DetailView  
from django.views.generic.edit import CreateView, UpdateView, DeleteView  
from django.urls import reverse_lazy  
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate 
from .models import Cita, Mascota
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django import forms
from django.contrib.auth.mixins import UserPassesTestMixin


def admin_required(function):
    return user_passes_test(lambda u: u.is_superuser)(function)

def login_request(request):

    if request.method == "POST": 
        form = AuthenticationForm(request, data=request.POST)  
        print(form) 

        if form.is_valid():
            usuario = form.cleaned_data.get("username") 
            clave = form.cleaned_data.get("password") 

            nombre_usuario = authenticate(username=usuario, password=clave) 

            if nombre_usuario is not None:  
                login(request, nombre_usuario)  
                return render(request, "AppLitobar/index.html", {"mensaje":f"Has iniciado sesión. Bienvenido {usuario}"})  
            else:  
                form = AuthenticationForm()  
                return render(request, "AppLitobar/login.html", {"mensaje":"Error, datos incorrectos", "form": form})  
        else:  
            return render(request, "AppLitobar/index.html", {"mensaje":"Error, formulario inválido"}) 

    form = AuthenticationForm()  
    return render(request, "AppLitobar/login.html", {"form":form})  





class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ["fecha", "motivo", "veterinario", "imagen_mascota"]

class CitaFormNoImage(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ["fecha", "motivo", "veterinario"]

class CitaListView(LoginRequiredMixin, ListView):
    model = Cita 
    template_name = "AppLitobar/Vistas_Clases/cita_list.html"


class CitaDetalle(LoginRequiredMixin, DetailView):
    model = Cita
    template_name = "AppLitobar/Vistas_Clases/cita_detalle.html"


class CitaCreateView(LoginRequiredMixin, CreateView):
    model = Cita
    template_name = "AppLitobar/Vistas_Clases/cita_form.html"
    success_url = reverse_lazy("List")

    def get_form_class(self):
        if self.request.user.is_superuser:
            return CitaForm
        else:
            return CitaFormNoImage
    

class CitaUpdateView(LoginRequiredMixin, UpdateView):
    model = Cita
    template_name = "AppLitobar/Vistas_Clases/cita_edit.html"
    success_url = reverse_lazy("List")

    def get_form_class(self):
        if self.request.user.is_superuser:
            return CitaForm
        else:
            return CitaFormNoImage
    


class CitaDeleteView(LoginRequiredMixin, DeleteView):
    model = Cita
    success_url = reverse_lazy("List")
    template_name = "AppLitobar/Vistas_Clases/cita_confirm_delete.html"  





#mascotas vistas 

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ["nombre_mascota", "tipo", "raza", "fecha_nacimiento", "edad", "imagen"]



class MascotasListView(LoginRequiredMixin, ListView):
    model = Mascota  
    template_name = "AppLitobar/Vistas_Clases/mascotas_list.html" 


class MascotasDetalle(LoginRequiredMixin, DetailView):
    model = Mascota
    template_name = "AppLitobar/Vistas_Clases/mascotas_detalle.html"
    context_object_name = 'mascota'

class MascotasCreateView(LoginRequiredMixin, CreateView):
    model = Mascota
    form_class = MascotaForm
    template_name = "AppLitobar/Vistas_Clases/mascotas_form.html"
    success_url = reverse_lazy("Lista")

    def get_form_class(self):
        if self.request.user.is_superuser:
            return MascotaForm
        else:
            class MascotaFormNoImage(forms.ModelForm):
                class Meta:
                    model = Mascota
                    fields = ["nombre_mascota", "tipo", "raza", "fecha_nacimiento", "edad"]
            return MascotaFormNoImage
        


class MascotasUpdateView(LoginRequiredMixin, UpdateView):
    model = Mascota
    form_class = MascotaForm
    template_name = "AppLitobar/Vistas_Clases/mascotas_edit.html"
    success_url = reverse_lazy("Lista")

    def get_form_class(self):
        if self.request.user.is_superuser:
            return MascotaForm
        else:
            class MascotaFormNoImage(forms.ModelForm):
                class Meta:
                    model = Mascota
                    fields = ["nombre_mascota", "tipo", "raza", "fecha_nacimiento", "edad"]
            return MascotaFormNoImage



class MascotasDeleteView(LoginRequiredMixin, DeleteView):
    model = Mascota
    success_url = reverse_lazy("Lista")  
    template_name = "AppLitobar/Vistas_Clases/mascotas_confirm_delete.html"  
