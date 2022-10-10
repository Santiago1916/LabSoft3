from django.db import models

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
    nombre = models.TextField(max_length = 50, verbose_name = 'Nombre Coctel')
    sinoAlcohol =  models.BooleanField(default = 'True')

    def coctelDatos(self):
        return "{} {}, {}".format(self.id,  self.nombre , self.sinoAlcohol)
    
    def __str__(self):
        return self.coctelDatos()

class Licor(models.Model):
    id = models.BigAutoField(auto_created = True, primary_key = True, serialize = False, verbose_name = 'ID')
    nombre = models.TextField(max_length = 50, verbose_name = 'Nombre del licor')
    cantidad = models.IntegerField(verbose_name = 'Cantidad en ml del licor')

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
    idLicorBase = models.ForeignKey(Licor, null = True, blank = True, on_delete = models.CASCADE)
    idDiluidores = models.ForeignKey(Diluidores, null = True, blank = True, on_delete = models.CASCADE)

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