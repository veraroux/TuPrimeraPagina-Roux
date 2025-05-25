from django.urls import path
from .views import lista_cultural, lista_diseño, lista_gastronomia, lista_nocturno, lista_rubros, gastronomiaForm, culturalForm, nocturnoForm, diseñoForm, buscar_gastronomia

urlpatterns = [
    
    path('', lista_rubros, name='lista_rubros'),

    path('cultural/', lista_cultural, name='lista_cultural'),
  
    path('diseño/', lista_diseño, name='lista_diseño'),

    path('gastronomia/', lista_gastronomia, name='lista_gastronomia'),

    path('nocturno/', lista_nocturno, name='lista_nocturno'),

    path('gastronomia_form/', gastronomiaForm, name='gastronomia_form'),

    path('cultural_form/', culturalForm, name= 'cultural_form'),

    path('nocturno_form/', nocturnoForm, name= 'nocturno_form'),

    path('diseño_form/', diseñoForm, name= 'diseño_form'),

    path('buscar_gastronomia/', buscar_gastronomia, name='buscar_gastronomia'),



]