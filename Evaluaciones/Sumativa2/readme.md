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
2. cd evaluaciones/sumativa2/gestion_productos
3. Ejecuta la aplicación con 
               
      python manage.py runserver.

## Uso
- Visita `http://127.0.0.1:8000/` para navergar entre los templates
- Visita `http://127.0.0.1:8000/registro/` para registrar un producto.
- Visita `http://127.0.0.1:8000/consulta/` para ver los productos registrados.
- Visita `http://127.0.0.1:8000/admin` para ingresar como administrador 



