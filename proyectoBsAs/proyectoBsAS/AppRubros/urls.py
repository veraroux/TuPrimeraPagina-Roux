from django.urls import path
from .views import *
from . import views
from django.contrib.auth.views import LogoutView


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

    path('acerca_de_mi', acerca_de_mi, name= 'acerca_de_mi'),

    path('cultural/<int:pk>/', cultural_detail, name='cultural_detail'),
    
    path('gastronomia/<int:pk>/', gastronomia_detail, name='gastronomia_detail'),

    path('nocturno/<int:pk>/', nocturno_detail, name='nocturno_detail'),

    path('diseño/<int:pk>/', diseño_detail, name='diseño_detail'),

    path('buscar_cultura/', buscar_cultural, name='buscar_cultural'),

    path('buscar_diseño/', buscar_diseño, name='buscar_diseño'),

    path('buscar_nocturno/', buscar_nocturno, name='buscar_nocturno'),

    path('bienvenida/', BienvenidaView.as_view(), name='bienvenida'),

    path('registro/', Registrarse.as_view() , name="registro"),

    path('login/', loginRequest, name='login'),

    path('edicionPerfil/', editar_perfil_completo, name='editar_perfil'),

    path('cambiar_contraseña/', ContraseñaCambiar.as_view(), name='cambiar_contraseña'),

    path('contraseña_cambio_exitoso/' , views.password_exitoso, name='contraseña_cambio_exitoso'),

    path('logout/', LogoutView.as_view(), name='logout'),

    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),

    path("gastronomiaUpdate/<int:pk>/",  views.GastronomiaUpdate.as_view() , name="gastronomiaUpdate"),
    path("gastronomiaDelete/<int:pk>/",  views.GastronomiaDelete.as_view() , name="gastronomiaDelete"),

    path("diseñoUpdate/<int:pk>/",  views.DiseñoUpdate.as_view() , name="diseñoUpdate"),
    path("diseñoDelete/<int:pk>/",  views.DiseñoDelete.as_view() , name="diseñoDelete"),

    path("nocturnoUpdate/<int:pk>/",  views.NocturnoUpdate.as_view() , name="nocturnoUpdate"),
    path("nocturnoDelete/<int:pk>/",  views.NocturnoDelete.as_view() , name="nocturnoDelete"),

    path("culturalUpdate/<int:pk>/",  views.CulturalUpdate.as_view() , name="culturalUpdate"),
    path("culturalDelete/<int:pk>/",  views.CulturalDelete.as_view() , name="culturalDelete"),



]