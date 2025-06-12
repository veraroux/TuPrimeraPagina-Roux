from django.db import models
from datetime import date
from django.contrib.auth.models import User


class Gastronomia (models.Model):
    nombre = models.CharField(max_length=200)
    barrio = models.CharField(max_length=200)
    direccion = models.CharField (max_length= 200)
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    reseña = models.CharField (max_length= 1000)
    foto = models.ImageField(upload_to='fotos_locales/', blank=True, null=True)  





    def __str__(self):
        return f"nombre: {self.nombre}, barrio: {self.barrio}"
    
    @property
    def presentacion_completa (self): 
          return (f"Nombre: {self.nombre}<br> Barrio: {self.barrio}<br> Direccion: {self.direccion}")
    

class Cultural (models.Model):
    nombre = models.CharField(max_length=200)
    barrio = models.CharField(max_length=200)
    direccion = models.CharField (max_length= 200)
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    reseña = models.CharField (max_length= 1000)
    foto = models.ImageField(upload_to='fotos_locales/', blank=True, null=True)  






    def __str__(self):
        return f"nombre: {self.nombre}, barrio: {self.barrio}"
    
    def presentacion_completa (self): 
          return (f"Nombre: {self.nombre}<br> Barrio: {self.barrio}<br> Direccion: {self.direccion}")


class Nocturno (models.Model):
    nombre = models.CharField(max_length=200)
    barrio = models.CharField(max_length=200)
    direccion = models.CharField (max_length= 200)
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    reseña = models.CharField (max_length= 1000)
    foto = models.ImageField(upload_to='fotos_locales/', blank=True, null=True)  





    def __str__(self):
        return f"nombre: {self.nombre}, barrio: {self.barrio}"
    
    def presentacion_completa (self): 
          return (f"Nombre: {self.nombre}<br> Barrio: {self.barrio}<br> Direccion: {self.direccion}")


class Diseño (models.Model):
    nombre = models.CharField(max_length=200)
    barrio = models.CharField(max_length=200)
    direccion = models.CharField (max_length= 200)
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    reseña = models.CharField (max_length= 1000)
    foto = models.ImageField(upload_to='fotos_locales/', blank=True, null=True)  





class Avatar(models.Model):   
    imagen = models.ImageField(upload_to="avatares") 
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"    
# Create your models here.
