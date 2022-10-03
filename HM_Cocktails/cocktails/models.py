from django.db import models
from .choices import SinoCon

# Create your models here.
class usuario(models.Model):
    nombre = models.CharField(max_length = 50, verbose_name = 'Nombre usuario')
    apellido = models.CharField(max_length = 50, verbose_name = 'Apellido usuario')
    nombreDeUsuario = models.CharField(max_length = 50, verbose_name = 'Nombre de usuario')
    fechaNacimiento = models.DateField(verbose_name= 'Fecha nacimiento usuario')
    """idListaFavoritos = models.ForeignKey(favoritos, null = True, blank = True)"""
    campo = models.CharField(max_length = 50, verbose_name = 'Campo Usuario')

    def usuarioDatos(self):
        return "{}, {} {} {}".format(self.id, self.nombreDeUsuario, self.nombre, self.apellido)

    def __str__(self):
        return self.usuarioDatos()

class componente(models.Model):
    nombre = models.CharField(max_length = 50, verbose_name = 'Nombre componente')
    tipoComponente = models.CharField(max_length = 50, verbose_name = 'Tipo componente')

    def componenteDatos(self):
        return "{}, {} {}".format(self.id, self.nombre, self.tipoComponente)

    def __str__(self):
        return self.componenteDatos()

class coctel(models.Model):
    nombre = models.TextField(blank = True)
    idComponente = models.ForeignKey(componente, null = True, blank = True, on_delete = models.CASCADE)
    sinoAlcohol =  models.CharField(max_length = 2, choices = SinoCon, default = 'Si')
    '''favorito = models.ForeignKey(favoritos, null = True, blank = True)'''

    def coctelDatos(self):
        return "{} {}, {}".format(self.id,  self.nombre , self.sinoAlcohol)
    
    def __str__(self):
        return self.coctelDatos()

class favoritos(models.Model):
    idUsuario = models.ForeignKey(usuario,null = True, blank = True, on_delete = models.CASCADE)
    idCoctel = models.ForeignKey(coctel,null = True, blank = True, on_delete = models.CASCADE)

    def favoritosDatos(self):
        return "{}, {}, {}".format(self.id,  self.idUsuario , self.idCoctel)
    
    def __str__(self):
        return self.favoritosDatos()


""" Relaciones Foraneas entre modelos -> https://www.youtube.com/watch?v=y89VHGofsDQ"""
'''Django & PostgreSQL CRUD -> https://www.youtube.com/watch?v=_zNZ1lK6RTA'''