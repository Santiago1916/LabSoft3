from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    idUsuario = models.CharField(max_length=100, blank=True, null=True)

    def say_hello(self):
        return "Hola, mi usuario es {}".format(self.first_name)

    def __str__(self):
        return f'{self.username}'

class CategoriaCoctel(models.Model):
    nombreCategoria = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Categoria Coctel'
        verbose_name_plural = 'Categoria de cocteles'
    
    def __str__(self):
        return f'{self.nombreCategoria}'

    @property
    def contarCoctelesPorCategoria(self):
        return Coctel.objects.filter(category=self).count()

class Coctel(models.Model):
    id = models.BigAutoField(auto_created = True, primary_key = True, serialize = False, verbose_name = 'ID') 
    nombre = models.TextField(max_length = 50, verbose_name = 'Nombre Coctel')
    sinoAlcohol =  models.BooleanField(default = 'True')
    categoria = models.ForeignKey(CategoriaCoctel, on_delete=models.CASCADE, related_name="Cocteles categoria")

    def coctelDatos(self):
        return "{} {}, {}".format(self.id,  self.nombre , self.sinoAlcohol)
    
    def __str__(self):
        return f'{self.nombre}- categoria: {self.categoria}'

class Imagen(models.Model):
    coctel = models.ForeignKey(Coctel, on_delete=models.CASCADE, related_name='Obtener Imagen')
    imagen = models.ImageField(upload_to='images/')

    def __str__(self):
        return f'{self.imagen}'

class Licor(models.Model):
    id = models.BigAutoField(auto_created = True, primary_key = True, serialize = False, verbose_name = 'ID')
    nombre = models.TextField(max_length = 50, verbose_name = 'Nombre del licor')
    cantidad = models.IntegerField(verbose_name = 'Cantidad en ml del licor', default=0)

    def licorDatos(self):
        return "{}, {} {}".format(self.id,  self.nombre , self.cantidad)
    
    def __str__(self):
        return self.coctelDatos()

class Diluidores(models.Model):
    id = models.BigAutoField(auto_created = True, primary_key = True, serialize = False, verbose_name = 'ID')
    nombre = models.TextField(max_length = 50, verbose_name = 'Nombre del diluidor')
    cantidad = models.IntegerField(verbose_name = 'Cantidad')

    def diluidoresDatos(self):
        return "{}, {} {}".format(self.id,  self.nombre , self.cantidad)
    
    def __str__(self):
        return self.diluidoresDatos()

class ComponentesCoctel(models.Model):
    id = models.BigAutoField(auto_created = True, primary_key = True, serialize = False, verbose_name = 'ID')
    idCoctel = models.ForeignKey(Coctel, null = True, blank = True, on_delete = models.CASCADE)
    idLicorBase = models.ManyToManyField(Licor, null = True, blank = True, on_delete = models.CASCADE)
    idDiluidores = models.ManyToManyField(Diluidores, null = True, blank = True, on_delete = models.CASCADE)

    def componenteDatos(self):
        return "{} {}, {} {} {}".format(self.id, self.idCoctel, self.idLicorBase, self.idLicorSecundario, self.idDiluidores)

    def __str__(self):
        return self.componenteDatos()
        
class Favoritos(models.Model):
    id = models.BigAutoField(auto_created = True, primary_key = True, serialize = False, verbose_name = 'ID') 
    idUsuario = models.ForeignKey(Usuario, null = True, blank = True, on_delete = models.CASCADE)
    idCoctel = models.ForeignKey(Coctel, null = True, blank = True, on_delete = models.CASCADE)

    def favoritosDatos(self):
        return "{}, {}, {}".format(self.id,  self.idUsuario , self.idCoctel)
    
    def __str__(self):
        return self.favoritosDatos()




""" Relaciones Foraneas entre modelos -> https://www.youtube.com/watch?v=y89VHGofsDQ"""
'''Django & PostgreSQL CRUD -> https://www.youtube.com/watch?v=_zNZ1lK6RTA'''