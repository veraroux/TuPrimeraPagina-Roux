from django.shortcuts import render, get_object_or_404
from.models import Gastronomia, Nocturno, Cultural, Diseño
from.forms import *
from django.http import HttpResponse

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

def gastronomiaForm(request): 
    if request.method == "POST":
        form = GastronomiaForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            barrio = form.cleaned_data["barrio"]
            direccion = form.cleaned_data["direccion"]
            local = Gastronomia(nombre=nombre, barrio=barrio, direccion=direccion)
            local.save()
            gastronomia = Gastronomia.objects.all()
            return render(request, 'AppRubros/gastronomia_lista.html',{"gastronomia": gastronomia} )
    else:
        form = GastronomiaForm()
    return render(request, "AppRubros/gastronomia_form.html", {"form": form})


def culturalForm (request): 
    if request.method == "POST":
        form = CulturalForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            barrio = form.cleaned_data["barrio"]
            direccion = form.cleaned_data["direccion"]
            local = Cultural(nombre=nombre, barrio=barrio, direccion=direccion)
            local.save()
            cultural = Cultural.objects.all()
            return render(request, 'AppRubros/cultural_lista.html',{"cultural": cultural} )
    else:
        form =CulturalForm()
    return render(request, "AppRubros/cultural_form.html", {"form": form})

def nocturnoForm (request): 
    if request.method == "POST":
        form = NocturnoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            barrio = form.cleaned_data["barrio"]
            direccion = form.cleaned_data["direccion"]
            local = Nocturno(nombre=nombre, barrio=barrio, direccion=direccion)
            local.save()
            nocturno = Nocturno.objects.all()
            return render(request, 'AppRubros/nocturno_lista.html',{"nocturno": nocturno} )
    else:
        form =NocturnoForm()
    return render(request, "AppRubros/nocturno_form.html", {"form": form})

def diseñoForm (request): 
    if request.method == "POST":
        form = DiseñoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            barrio = form.cleaned_data["barrio"]
            direccion = form.cleaned_data["direccion"]
            local = Diseño(nombre=nombre, barrio=barrio, direccion=direccion)
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
# Create your views here.
