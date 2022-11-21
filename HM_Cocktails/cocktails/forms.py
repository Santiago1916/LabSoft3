from django import forms

from .models import Coctel, Licor,Diluidores, ComponentesCoctel, Imagen

class ModeloCoctel(forms.ModelForm):
    class Meta:
        modelo = Coctel
        modelo2 = Licor
        modelo3 = Diluidores
        modelo4 = comp
        campos = ['nombreCoctel', 'sinoAlcohol', 'nombreLicor', 'cantidadLicor', 'nombreDiluidor', 'cantidadDiluidor', 'categoria']

    def _init_(self, *args, **kwargs):
        super(ModeloCoctel, self)._init_(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class ModeloImagen(forms.ModelForm):
    class Meta:
        modelo = Imagen
        campo = ['imagen']

    def _init_(self, *args, **kwargs):
        super(ModeloImagen, self)._init_(*args, **kwargs)
        self.visible_fields()[0].field.widget.attrs['class'] ='form-control'
