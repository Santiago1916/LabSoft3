from django.db import models
from .choices import SinoCon

# Create your models here.
class Usuario(models.Model):
    id = models.BigAutoField(auto_created = True, primary_key = True, serialize = False, verbose_name = 'ID')                
    nombre = models.CharField(max_length = 50, verbose_name = 'Nombre usuario')
    apellido = models.CharField(max_length = 50, verbose_name = 'Apellido usuario')
    nombreDeUsuario = models.CharField(max_length = 50, verbose_name = 'Nombre de usuario')
    fechaNacimiento = models.DateField(verbose_name= 'Fecha nacimiento usuario')

    def usuarioDatos(self):
        return "{}, {} {} {}".format(self.id, self.nombreDeUsuario, self.nombre, self.apellido)

    def __str__(self):
        return self.usuarioDatos()
        
class Coctel(models.Model):
    id = models.BigAutoField(auto_created = True, primary_key = True, serialize = False, verbose_name = 'ID') 
    nombre = models.TextField(blank = True)
    sinoAlcohol =  models.CharField(max_length = 2, choices = SinoCon, default = 'Si')

    def coctelDatos(self):
        return "{} {}, {}".format(self.id,  self.nombre , self.sinoAlcohol)
    
    def __str__(self):
        return self.coctelDatos()

class Ingrediente(models.Model):
    id = models.BigAutoField(auto_created = True, primary_key = True, serialize = False, verbose_name = 'ID')
    idCoctel = models.ForeignKey(Coctel, null = True, blank = True, on_delete = models.CASCADE)
    nombre = models.CharField(max_length = 50, verbose_name = 'Nombre del coctel')
    cantidad = models.CharField(max_length = 50, verbose_name = 'Cantidad del alcohol')
    tipoIngrediente = models.CharField(max_length = 50, verbose_name = 'Tipo componente')

    def componenteDatos(self):
        return "{}, {} {}".format(self.id, self.nombre, self.tipoComponente)

    def __str__(self):
        return self.componenteDatos()

class favoritos(models.Model):
    id = models.BigAutoField(auto_created = True, primary_key = True, serialize = False, verbose_name = 'ID') 
    idUsuario = models.ForeignKey(Usuario, null = True, blank = True, on_delete = models.CASCADE)
    idCoctel = models.ForeignKey(Coctel, null = True, blank = True, on_delete = models.CASCADE)

    def favoritosDatos(self):
        return "{}, {}, {}".format(self.id,  self.idUsuario , self.idCoctel)
    
    def __str__(self):
        return self.favoritosDatos()

""" Relaciones Foraneas entre modelos -> https://www.youtube.com/watch?v=y89VHGofsDQ"""
'''Django & PostgreSQL CRUD -> https://www.youtube.com/watch?v=_zNZ1lK6RTA'''