from  django import forms

class GastronomiaForm(forms.Form):
    nombre = forms.CharField(max_length=200, label="Nombre del sitio gastronomico", required=True)
    barrio = forms.CharField(max_length=200, label="Nombre del barrio donde se encuentra", required=True)
    direccion = forms.CharField(max_length=200, label="Direccion del local", required=True)

class CulturalForm(forms.Form):
     nombre = forms.CharField(max_length=200, label="Nombre del espacio cultural", required=True)
     barrio = forms.CharField(max_length=200, label="Nombre del barrio donde se encuentra", required=True)
     direccion = forms.CharField(max_length=200, label="Direccion del sitio", required=True)


class DiseñoForm(forms.Form):
    nombre = forms.CharField(max_length=200, label="Nombre del negocio", required=True)
    barrio = forms.CharField(max_length=200, label="Nombre del barrio donde se encuentra", required=True)
    direccion = forms.CharField(max_length=200, label="Direccion del local", required=True)

class NocturnoForm(forms.Form):
    nombre = forms.CharField(max_length=200, label="Nombre del sitio", required=True)
    barrio = forms.CharField(max_length=200, label="Nombre del barrio donde se encuentra", required=True)
    direccion = forms.CharField(max_length=200, label="Direccion del local", required=True)


class BuscarGastronomia(forms.Form): 
    consulta = forms.CharField(label= 'Buscar', max_length= 200)