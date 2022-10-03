from django.db import models
from .choices import SinoCon

# Create your models here.
class Usuario(models.Model):
    id = models.BigAutoField(auto_created = True, primary_key = True, serialize = False, verbose_name = 'ID')                
    nombre = models.CharField(max_length = 50, verbose_name = 'Nombre Usuario')
    apellido = models.CharField(max_length = 50, verbose_name = 'Apellido Usuario')
    nombreDeUsuario = models.CharField(max_length = 50, verbose_name = 'Nombre de Usuario')
    fechaNacimiento = models.DateField(verbose_name= 'Fecha nacimiento Usuario')
    '''idListaFavoritos = models.ForeignKey(Favoritos, null = True, blank = True)'''

    def UsuarioDatos(self):
        return "{}, {} {} {}".format(self.id, self.nombreDeUsuario, self.nombre, self.apellido)

    def __str__(self):
        return self.UsuarioDatos()

class Componente(models.Model):
    id = models.BigAutoField(auto_created = True, primary_key = True, serialize = False, verbose_name = 'ID') 
    nombre = models.CharField(max_length = 50, verbose_name = 'Nombre Componente')
    tipoComponente = models.CharField(max_length = 50, verbose_name = 'Tipo Componente')

    def ComponenteDatos(self):
        return "{}, {} {}".format(self.id, self.nombre, self.tipoComponente)

    def __str__(self):
        return self.ComponenteDatos()

class Coctel(models.Model):
    id = models.BigAutoField(auto_created = True, primary_key = True, serialize = False, verbose_name = 'ID') 
    nombre = models.TextField(blank = True)
    idComponente = models.ForeignKey(Componente, null = True, blank = True, on_delete = models.CASCADE)
    sinoAlcohol =  models.CharField(max_length = 2, choices = SinoCon, default = 'Si')
    '''favorito = models.ForeignKey(models.Favoritos, null = True, blank = True)'''

    def CoctelDatos(self):
        return "{} {}, {}".format(self.id,  self.nombre , self.sinoAlcohol)
    
    def __str__(self):
        return self.CoctelDatos()

class Favoritos(models.Model):
    id = models.BigAutoField(auto_created = True, primary_key = True, serialize = False, verbose_name = 'ID') 
    idUsuario = models.ForeignKey(Usuario,null = True, blank = True, on_delete = models.CASCADE)
    idCoctel = models.ForeignKey(Coctel,null = True, blank = True, on_delete = models.CASCADE)

    def FavoritosDatos(self):
        return "{}, {}, {}".format(self.id,  self.idUsuario , self.idCoctel)
    
    def __str__(self):
        return self.FavoritosDatos()


""" Relaciones Foraneas entre modelos -> https://www.youtube.com/watch?v=y89VHGofsDQ"""
'''Django & PostgreSQL CRUD -> https://www.youtube.com/watch?v=_zNZ1lK6RTA'''