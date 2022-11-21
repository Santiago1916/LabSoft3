from django.urls import path

from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('inicio de sesion', views.vistaInicioSesion, name='inicio de sesion'),
    path('cerrar sesion', views.vistaCierreInicioSesion, name='cerrar sesion'),
    path('registro', views.registro, name='register'),
]