from django.contrib import admin
from .models import Peliculas, Arriendos, Clientes, Usuarios

# Register your models here.

admin.site.register(Peliculas)
admin.site.register(Clientes)
admin.site.register(Arriendos)
admin.site.register(Usuarios)