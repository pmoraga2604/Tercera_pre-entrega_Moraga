from django.urls import path 
from AppVC.views import *
from . import views

urlpatterns = [

   path('arriendos/', arriendos, name='Arriendos'),
   path('clientes/', clientes, name='Clientes'),
   path('usuarios/', usuarios, name='Usuarios'),
   path('', peliculas, name='Peliculas'),
   path('lista-usuarios/', lista_usuarios),
   path('formulario-usuario/', formulario_usuario, name='FormularioUsuario'),
   path('formulario-reserva/', formulario_reserva, name='FormularioReserva'),
   path('agregar-cliente/', agregar_cliente, name='agregar_cliente'),
   path('lista-peliculas/', views.lista_peliculas, name='lista_peliculas'),
   path('arriendos-realizados/', views.arriendos_realizados, name='arriendos_realizados'),


]