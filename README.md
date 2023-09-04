# Tercera_pre-entrega_Moraga

El "proyecto", esta realizado en Django, HTML y Python. Donde se trabajo en la herencia de HTML compartiendo el header, navbar y formato desde archivos html centrales. De la misma manera se crearon html para incorporarlos con el metodo de herencia.
Actualmente tiene muchos archivos .html creados y views que no estan en uso dado que no supe como implementar todo lo que tenia pensado, pero es un avance y creo que cumple con los criterios de evaluacion propuestos para esta etapa.

Como navegar:

Posee en la parte superior izquierda  un drop-down con distintas opciones tales como : 
1.- Peliculas
2.- Clientes
3.- Arriendos
4.- Usuarios

(1) Peliculas
* Inician en http://127.0.0.1:8000/app-vc/, donde se desplega la informacion de las Peliculas existentes en la Base de datos en la tabla Peliculas, ademas pueden agregar Peliculas con el formulario ubicado en la misma pagina, las cuales se listaran automaticamente. El modelo se llama "Peliculas", la view tambien se llama "peliculas y el template se llama peliculas.html, el cual es llamado por la url con el "path('', peliculas, name='Peliculas'),".

(2) Clientes
* Consta de 3 funciones en la misma pagina, desde buscar clientes por nombre, listar los resultados de la busqueda y agregar un nuevo cliente a la base de datos.El template donde esta el codigo esta en "clientes.html" el cual tiene contenido heredado de otras paginas, ademas cuenta con 2 formularios registrados en forms.py, los cuales realizan busqueda de clientes y registro de clientes.

(3) Arriendos
* Se divide en tres partes, una de ellas lista la totalidad de clientes en la base de datos, otra parte lista todas las peliculas registradas en la base de datos y por ultimo realiza la reserva de peliculas asociando el id del cliente y el id de la pelicula, datos que se almacenan en la base de datos.

(4) Usuarios
Lista los usuarios en la base de datos y permmite mediante un formulario agregar un nuevo usuario.


  
