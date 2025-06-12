from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from AppRubros.models import Gastronomia, Nocturno, Cultural, Diseño, Avatar
from.forms import GastronomiaForm, DiseñoForm, NocturnoForm, CulturalForm, BuscarGastronomia, BuscarCultural, BuscarDiseño, BuscarNocturno, RegistroForm, FormEditarUsuario, FormCambioPassword, AvatarForm
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView 
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import login, update_session_auth_hash, authenticate
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required



class AcercaDeMiView(LoginRequiredMixin, TemplateView):
    template_name = 'acerca_de_mi.html'


def acerca_de_mi (request):

    return render(request, 'AppRubros/acerca_de_mi.html')


def lista_rubros(request):
    return render(request, 'AppRubros/rubros.html')

def lista_gastronomia (request):
    gastronomia = Gastronomia.objects.all()
    return render(request, 'AppRubros/gastronomia_lista.html', {'gastronomia': gastronomia})

def lista_nocturno (request):
    nocturno = Nocturno.objects.all()
    return render(request, 'AppRubros/nocturno_lista.html', {'nocturno': nocturno})

def lista_cultural (request):
    cultural= Cultural.objects.all()
    return render(request, 'AppRubros/cultural_lista.html', {'cultural': cultural})

def lista_diseño (request):
    diseño = Diseño.objects.all()
    return render(request, 'AppRubros/diseño_lista.html', {'diseño': diseño})

@login_required
def gastronomiaForm(request): 
    if request.method == "POST":
        form = GastronomiaForm(request.POST, request.FILES)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            barrio = form.cleaned_data["barrio"]
            direccion = form.cleaned_data["direccion"]
            reseña = form.cleaned_data["reseña"]
            fechaPublicacion = form.cleaned_data["fechaPublicacion"]
            foto = form.cleaned_data.get("foto")

            local = Gastronomia(nombre=nombre, barrio=barrio, direccion=direccion, reseña=reseña, fechaPublicacion=fechaPublicacion, foto=foto)
            local.save()
            gastronomia = Gastronomia.objects.all()
            return render(request, 'AppRubros/gastronomia_lista.html',{"gastronomia": gastronomia} )
    else:
        form = GastronomiaForm()
    return render(request, "AppRubros/gastronomia_form.html", {"form": form})

@login_required
def culturalForm (request): 
    if request.method == "POST":
        form = CulturalForm(request.POST, request.FILES)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            barrio = form.cleaned_data["barrio"]
            direccion = form.cleaned_data["direccion"]
            reseña = form.cleaned_data["reseña"]
            fechaPublicacion = form.cleaned_data["fechaPublicacion"]
            foto = form.cleaned_data.get("foto")


            local = Cultural(nombre=nombre, barrio=barrio, direccion=direccion, reseña=reseña, fechaPublicacion=fechaPublicacion, foto=foto)
            local.save()
            cultural = Cultural.objects.all()
            return render(request, 'AppRubros/cultural_lista.html',{"cultural": cultural} )
    else:
        form =CulturalForm()
    return render(request, "AppRubros/cultural_form.html", {"form": form})

@login_required
def nocturnoForm (request): 
    if request.method == "POST":
        form = NocturnoForm(request.POST, request.FILES)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            barrio = form.cleaned_data["barrio"]
            direccion = form.cleaned_data["direccion"]
            reseña = form.cleaned_data["reseña"]
            fechaPublicacion = form.cleaned_data["fechaPublicacion"]
            foto = form.cleaned_data.get("foto")

            local = Nocturno(nombre=nombre, barrio=barrio, direccion=direccion, reseña=reseña, fechaPublicacion=fechaPublicacion, foto=foto)
            local.save()
            nocturno = Nocturno.objects.all()
            return render(request, 'AppRubros/nocturno_lista.html',{"nocturno": nocturno} )
    else:
        form =NocturnoForm()
    return render(request, "AppRubros/nocturno_form.html", {"form": form})

@login_required
def diseñoForm (request): 
    if request.method == "POST":
        form = DiseñoForm(request.POST, request.FILES)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            barrio = form.cleaned_data["barrio"]
            direccion = form.cleaned_data["direccion"]
            reseña = form.cleaned_data["reseña"]
            fechaPublicacion = form.cleaned_data["fechaPublicacion"]
            foto = form.cleaned_data.get("foto")


            local = Diseño(nombre=nombre, barrio=barrio, direccion=direccion, reseña=reseña,fechaPublicacion=fechaPublicacion , foto=foto)
            local.save()
            diseño = Diseño.objects.all()
            return render(request, 'AppRubros/diseño_lista.html',{"diseño": diseño} )
    else:
        form =DiseñoForm()
    return render(request, "AppRubros/diseño_form.html", {"form": form})



def buscar_gastronomia (request): 
     resultados = []
     if request.method == 'GET':
        form = BuscarGastronomia(request.GET)
        if form.is_valid():
            consulta = form.cleaned_data['consulta']
            resultados = Gastronomia.objects.filter(nombre__icontains=consulta)
     else:
        form = BuscarGastronomia()

     return render(request, 'AppRubros/buscar_gastronomia.html', {
             'form': form,
            'resultados': resultados
})


def buscar_diseño(request): 
     resultados = []
     if request.method == 'GET':
        form = BuscarDiseño(request.GET)
        if form.is_valid():
            consulta = form.cleaned_data['consulta']
            resultados = Diseño.objects.filter(nombre__icontains=consulta)
     else:
        form = BuscarDiseño()

     return render(request, 'AppRubros/buscar_diseño.html', {
             'form': form,
            'resultados': resultados
})



def buscar_nocturno (request): 
     resultados = []
     if request.method == 'GET':
        form = BuscarNocturno(request.GET)
        if form.is_valid():
            consulta = form.cleaned_data['consulta']
            resultados = Nocturno.objects.filter(nombre__icontains=consulta)
     else:
        form = BuscarNocturno()

     return render(request, 'AppRubros/buscar_nocturno.html', {
             'form': form,
            'resultados': resultados
})



def buscar_cultural (request): 
     resultados = []
     if request.method == 'GET':
        form = BuscarCultural(request.GET)
        if form.is_valid():
            consulta = form.cleaned_data['consulta']
            resultados = Cultural.objects.filter(nombre__icontains=consulta)
     else:
        form = BuscarCultural()

     return render(request, 'AppRubros/buscar_cultural.html', {
             'form': form,
            'resultados': resultados
})



def cultural_detail(request, pk):
    lugar = get_object_or_404(Cultural, pk=pk)
    return render(request, 'AppRubros/cultural_detail.html', {'lugar': lugar})

def gastronomia_detail(request, pk):
    lugar= get_object_or_404(Gastronomia,pk=pk)
    return render(request, 'AppRubros/gastronomia_detail.html', {'lugar': lugar})

def nocturno_detail(request, pk):
    lugar= get_object_or_404(Nocturno,pk=pk)
    return render(request, 'AppRubros/nocturno_detail.html', {'lugar': lugar})


def diseño_detail(request, pk):
    lugar= get_object_or_404(Diseño,pk=pk)
    return render(request, 'AppRubros/diseño_detail.html', {'lugar': lugar})


class GastronomiaUpdate(LoginRequiredMixin, UpdateView): 
    model = Gastronomia
    fields = ["nombre", "barrio", "direccion", "reseña"]
    success_url = reverse_lazy("lista_gastronomia")

class DiseñoUpdate(LoginRequiredMixin, UpdateView): 
    model = Diseño
    fields = ["nombre", "barrio", "direccion", "reseña"]
    success_url = reverse_lazy("lista_diseño")

class NocturnoUpdate(LoginRequiredMixin, UpdateView): 
    model = Nocturno
    fields = ["nombre", "barrio", "direccion", "reseña"]
    success_url = reverse_lazy("lista_nocturno")

class CulturalUpdate(LoginRequiredMixin, UpdateView): 
    model = Cultural
    fields = ["nombre", "barrio", "direccion", "reseña"]
    success_url = reverse_lazy("lista_cultural")

class GastronomiaDelete(LoginRequiredMixin, DeleteView):
    model= Gastronomia
    template_name = "AppRubros/gastronomia_confirm_delete.html"
    success_url = reverse_lazy("lista_gastronomia")

class DiseñoDelete(LoginRequiredMixin, DeleteView):
    model= Diseño
    template_name = "AppRubros/diseño_confirm_delete.html"
    success_url = reverse_lazy("lista_diseño")

class CulturalDelete(LoginRequiredMixin, DeleteView):
    model= Cultural
    template_name = "AppRubros/cultural_confirm_delete.html"
    success_url = reverse_lazy("lista_cultural")

class NocturnoDelete(LoginRequiredMixin, DeleteView):
    model= Nocturno
    template_name = "AppRubros/nocturno_confirm_delete.html"
    success_url = reverse_lazy("lista_nocturno")








class BienvenidaView(LoginRequiredMixin, TemplateView):
    template_name = 'AppRubros/bienvenida.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usuario'] = self.request.user
        return context

def loginRequest(request):
   if request.method == "POST":
        usuario = request.POST["username"]
        clave = request.POST["password"]
        user = authenticate(request, username=usuario, password=clave)

        if user is not None:
            login(request, user)

            cargar_avatar_en_sesion(request)

            return redirect("bienvenida")
        else:
            return redirect(reverse_lazy('login'))
   else:
        miForm = AuthenticationForm()

   return render(request, "AppRubros/login.html", {"form": miForm})

class Registrarse(FormView):
    template_name = 'AppRubros/registro.html'
    form_class = RegistroForm
    redirect_autheticated_user = True
    success_url = reverse_lazy('bienvenida')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Registrarse, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(Registrarse, self).get(*args, **kwargs)


class UsuarioEditar(UpdateView):
    form_class = FormEditarUsuario
    template_name= 'AppRubros/editar_perfil.html'
    success_url = reverse_lazy('bienvenida')

    def get_object(self):
        return self.request.user

class ContraseñaCambiar(PasswordChangeView):
    form_class = FormCambioPassword
    template_name = 'AppRubros/cambiar_contraseña.html'
    success_url = reverse_lazy('contraseña_cambio_exitoso')

def password_exitoso(request):
    return render(request, 'AppRubros/contraseña_cambio_exitoso.html', {})


@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)
        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
            imagen = miForm.cleaned_data["imagen"]

            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
        

            
            avatar = Avatar(user=usuario, imagen=imagen)
            avatar.save()

            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            
            return redirect(reverse_lazy("bienvenida"))
    else:
        miForm = AvatarForm()
    return render(request, "AppRubros/agregar_avatar.html", {"form": miForm})    


@login_required
def editar_perfil_completo(request):
    user = request.user

    if request.method == 'POST':
        if 'perfil_submit' in request.POST:
            perfil_form = FormEditarUsuario(request.POST, instance=user)
            password_form = FormCambioPassword(user=user)  

            if perfil_form.is_valid():
                perfil_form.save()
                return redirect('bienvenida')

        elif 'password_submit' in request.POST:
            perfil_form = FormEditarUsuario(instance=user)
            password_form = FormCambioPassword(user=user, data=request.POST)

            if password_form.is_valid():
                password_form.save()
                update_session_auth_hash(request, user)
                return redirect('contraseña_cambio_exitoso')

    else:
        perfil_form = FormEditarUsuario(instance=user)
        password_form = FormCambioPassword(user=user)

    return render(request, 'AppRubros/editar_perfil.html', {
        'perfil_form': perfil_form,
        'password_form': password_form,
    })

def cargar_avatar_en_sesion(request):
    try:
        avatar = Avatar.objects.get(user=request.user)
        request.session["avatar"] = avatar.imagen.url
    except Avatar.DoesNotExist:
        request.session["avatar"] = "/media/avatares/default.png"
# Create your views here.


