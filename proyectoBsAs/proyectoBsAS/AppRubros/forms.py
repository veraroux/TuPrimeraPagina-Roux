from  django import forms
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User

class GastronomiaForm(forms.Form):
    nombre = forms.CharField(max_length=200, label="Nombre del sitio gastronomico", required=True)
    barrio = forms.CharField(max_length=200, label="Nombre del barrio donde se encuentra", required=True)
    direccion = forms.CharField(max_length=200, label="Direccion del local", required=True)
    fechaPublicacion = forms.DateTimeField(
        label="Fecha de publicación",
        required=True,
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )
    reseña = forms.CharField(max_length=1000, label="Reseña", required=True)
    foto = forms.ImageField(label="Foto del local", required=False) 

class CulturalForm(forms.Form):
     nombre = forms.CharField(max_length=200, label="Nombre del espacio cultural", required=True)
     barrio = forms.CharField(max_length=200, label="Nombre del barrio donde se encuentra", required=True)
     direccion = forms.CharField(max_length=200, label="Direccion del sitio", required=True)
     fechaPublicacion = forms.DateTimeField(
        label="Fecha de publicación",
        required=True,
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )
     reseña = forms.CharField(max_length=1000, label="Reseña", required=True)
     foto = forms.ImageField(label="Foto del local", required=False) 



class DiseñoForm(forms.Form):
    nombre = forms.CharField(max_length=200, label="Nombre del negocio", required=True)
    barrio = forms.CharField(max_length=200, label="Nombre del barrio donde se encuentra", required=True)
    direccion = forms.CharField(max_length=200, label="Direccion del local", required=True)
    fechaPublicacion = forms.DateTimeField(
        label="Fecha de publicación",
        required=True,
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )
    reseña = forms.CharField(max_length=1000, label="Reseña", required=True)
    foto = forms.ImageField(label="Foto del local", required=False) 

class NocturnoForm(forms.Form):
    nombre = forms.CharField(max_length=200, label="Nombre del sitio", required=True)
    barrio = forms.CharField(max_length=200, label="Nombre del barrio donde se encuentra", required=True)
    direccion = forms.CharField(max_length=200, label="Direccion del local", required=True)
    fechaPublicacion = forms.DateTimeField(
        label="Fecha de publicación",
        required=True,
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )
    reseña = forms.CharField(max_length=1000, label="Reseña", required=True)
    foto = forms.ImageField(label="Foto del local", required=False) 


class BuscarGastronomia(forms.Form): 
    consulta = forms.CharField(label= 'Buscar', max_length= 200)

class BuscarDiseño(forms.Form): 
    consulta = forms.CharField(label= 'Buscar', max_length= 200)

class BuscarNocturno(forms.Form): 
    consulta = forms.CharField(label= 'Buscar', max_length= 200)

class BuscarCultural(forms.Form): 
    consulta = forms.CharField(label= 'Buscar', max_length= 200)

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Contraseña a confirmar", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields =["username", "email", "password1", "password2"]

class FormEditarUsuario(UserChangeForm):
    password = None
    email = forms.EmailField(required=True)
    first_name = forms.CharField(label="Nombre", max_length=50, required=True)
    last_name = forms.CharField(label="Apellido", max_length=50, required=True)
    username = forms.CharField(label="Usuario", max_length=50, required=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name']

class FormCambioPassword(PasswordChangeForm):
    contra_actual = forms.CharField(label=("Contraseña Actual"),
                                   widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1 = forms.CharField(label=("Nueva Contraseña"),
                                   widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2 = forms.CharField(label=("Repita Nueva Contraseña"),
                                   widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['contra_actual', 'new_password1', 'new_password2']

class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)         