from django.contrib import admin

# Register your models here.
from .models import Usuario, CategoriaCoctel, Coctel, Imagen, Licor, Diluidores, ComponentesCoctel, Favoritos

admin.site.register(Usuario)
admin.site.register(CategoriaCoctel)
admin.site.register(Coctel)
admin.site.register(Imagen)
admin.site.register(Licor)
admin.site.register(Diluidores)
admin.site.register(ComponentesCoctel)
admin.site.register(Favoritos)