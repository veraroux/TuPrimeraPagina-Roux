from django.db import models

class Gastronomia (models.Model):
    nombre = models.CharField(max_length=200)
    barrio = models.CharField(max_length=200)
    direccion = models.CharField (max_length= 200)

    def __str__(self):
        return f"nombre: {self.nombre}, barrio: {self.barrio}"
    
    @property
    def presentacion_completa (self): 
          return (f"Nombre: {self.nombre}<br> Barrio: {self.barrio}<br> Direccion: {self.direccion}")
    

class Cultural (models.Model):
    nombre = models.CharField(max_length=200)
    barrio = models.CharField(max_length=200)
    direccion = models.CharField (max_length= 200)

    def __str__(self):
        return f"nombre: {self.nombre}, barrio: {self.barrio}"
    
    def presentacion_completa (self): 
          return (f"Nombre: {self.nombre}<br> Barrio: {self.barrio}<br> Direccion: {self.direccion}")


class Nocturno (models.Model):
    nombre = models.CharField(max_length=200)
    barrio = models.CharField(max_length=200)
    direccion = models.CharField (max_length= 200)

    def __str__(self):
        return f"nombre: {self.nombre}, barrio: {self.barrio}"
    
    def presentacion_completa (self): 
          return (f"Nombre: {self.nombre}<br> Barrio: {self.barrio}<br> Direccion: {self.direccion}")


class Diseño (models.Model):
    nombre = models.CharField(max_length=200)
    barrio = models.CharField(max_length=200)
    direccion = models.CharField (max_length= 200)

    def __str__(self):
    
        return f"nombre: {self.nombre}, barrio: {self.barrio}"   
    
    def presentacion_completa (self): 
          return (f"Nombre: {self.nombre}<br> Barrio: {self.barrio}<br> Direccion: {self.direccion}")

# Create your models here.
