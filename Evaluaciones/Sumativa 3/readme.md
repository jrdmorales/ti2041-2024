# Proyecto de Gestión de Productos

Este proyecto es una aplicación web desarrollada en Django para la empresa ficticia "Gestión de Productos S.A.". La aplicación permite a los administradores registrar y consultar datos básicos de productos.

## Estructura del Proyecto

- `gestion_productos/`: Contiene la configuración principal del proyecto Django.
- `productos/`: Contiene la aplicación para gestionar los productos.
- `templates/`: Contiene las plantillas HTML para las vistas.
- `static/`: Contiene archivos estáticos como CSS.
- `manage.py`: Script de gestión del proyecto.

## Requisitos Previos

- Python 3.12.0 
- Django 5.1.1 

## Instrucciones para Ejecutar el Proyecto

1. Clona el repositorio:

       git clone https://github.com/jrdmorales/ti2041-2024.git

2. Por comando cambia de directorio

       cd Evaluaciones/sumativa 3/gestion_productos

3. Agrega al usuario Administrador  "admin" password "inacap2024"

       python manage.py createsuperuser 

4. Aplicar las migraciones de las tablas
       
       python manage.py migrate
   
5. Ejecuta la aplicación con 
               
         python manage.py runserver

## Vistas 

- Las vistas fueron modificadas cumpliendo estos 2 puntos 

1. Haber asegurado las vistas que requieran que el usuario deba estar autenticado
       - filtrar, listar, consulta
2. Haber asegurado las vistas que requieran que el usuario sea administrador
       - productos, registrar, consulta, filtrar, listar
 
## Uso


- Visita `http://127.0.0.1:8000/` para Logearte 

- `vistas para Administrador`

- Visita `http://127.0.0.1:8000/productos/` para navergar entre los templates 
- Visita `http://127.0.0.1:8000/registrar/` para registrar un producto.
- Visita `http://127.0.0.1:8000/consulta/` para ver los productos registrados.
- Visita `http://127.0.0.1:8000/admin/` para ingresar como administrador
- Visita `http://127.0.0.1:8000/filtrar/` para filtrar dentro de los registros
- Visita `http://127.0.0.1:8000/listar/` para listar los productor registrados

- `Vistas para usuario normales`
- Visita `http://127.0.0.1:8000/filtrar/` para filtrar dentro de los registros
- Visita `http://127.0.0.1:8000/listar/` para listar los productor registrados
- Visita `http://127.0.0.1:8000/consulta/` para ver los productos registrados.
