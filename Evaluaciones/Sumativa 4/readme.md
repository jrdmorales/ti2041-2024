# Proyecto de Gestión de Productos

Este proyecto es una aplicación web desarrollada en Django para la empresa ficticia "Gestión de Productos S.A.". La aplicación permite a los administradores registrar y consultar datos básicos de productos, además de filtrar y listar productos según diferentes criterios como marca y categoría.

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

2. Cambia de directorio:

       cd Evaluaciones/sumativa 4/gestion_productos

3. Crea un superusuario para acceder al panel administrativo:

       python manage.py createsuperuser 
       # Usuario: admin, Contraseña: inacap2024

4. Aplica las migraciones de las tablas:

       python manage.py migrate

5. Ejecuta el servidor local:

       python manage.py runserver

## Vistas

### Seguridad

1. Se asegura que las vistas que requieran autenticación sean accesibles solo para usuarios autenticados:
   - `filtrar`, `listar`
   
2. Se asegura que las vistas administrativas, que requieren permisos de administrador, estén restringidas:
   - `productos`, `registrar`, `filtrar`, `listar`

## Uso

- Visita `http://127.0.0.1:8000/` para iniciar sesión como usuario normal.
- Visita `http://127.0.0.1:8000/admin/` para ingresar como administrador.

## Vistas para Administrador

El administrador tiene acceso completo a las siguientes vistas:

- **Registrar Producto**: `http://127.0.0.1:8000/registrar/` para registrar un producto.
- **Filtrar Productos**: `http://127.0.0.1:8000/filtrar/` para filtrar productos por marca o categoría.
- **Listar Productos**: `http://127.0.0.1:8000/listar/` para listar los productos registrados.
- **Gestionar Productos**: `http://127.0.0.1:8000/productos/` para navegar entre los templates relacionados a la gestión de productos.

## Vistas para Usuarios Normales

Los usuarios no administradores pueden acceder a las siguientes vistas:

- **Filtrar Productos**: `http://127.0.0.1:8000/filtrar/` para filtrar productos por marca o categoría.
- **Listar Productos**: `http://127.0.0.1:8000/listar/` para ver la lista de productos registrados.

## API de Gestión de Productos

La aplicación incluye una API RESTful para interactuar con los productos. Los endpoints disponibles permiten realizar operaciones CRUD (crear, leer, actualizar, eliminar) en los productos. 

### Endpoints de la API

1. **GET /api/productos/**:
   - Obtiene la lista de todos los productos registrados.
   
2. **POST /api/productos/**:
   - Crea un nuevo producto. Se deben proporcionar los parámetros `codigo`, `nombre`, `precio`, `marca`, `categoria` y `caracteristicas`.
   
3. **GET /api/productos/{id}/**:
   - Obtiene los detalles de un producto específico por su `id`.
   
4. **PUT /api/productos/{id}/**:
   - Actualiza un producto existente. Se deben proporcionar los mismos parámetros que en el `POST`.
   
5. **DELETE /api/productos/{id}/**:
   - Elimina un producto específico por su `id`.

### Autenticación en la API

Para acceder a los endpoints de la API, el usuario debe estar autenticado. El sistema utiliza un token de autenticación basado en JWT (JSON Web Tokens). Asegúrate de incluir el token en el encabezado `Authorization` de cada solicitud.

## Funcionalidades

- **Registro de Productos**: Los administradores pueden registrar productos con los siguientes atributos: código, nombre, precio, marca, categoría, y características.
- **Filtrado de Productos**: Los usuarios pueden filtrar productos por marca y categoría.
- **Consulta y Listado**: Los productos pueden ser consultados y listados con opciones de filtrado para facilitar la búsqueda.
- **Interacción con la API**: Se puede interactuar con los productos a través de la API para realizar operaciones CRUD.

- **Documentacion API**

       http://127.0.0.1:8000/api/docs


## Notas

- Los productos se pueden registrar con diferentes categorías y marcas que se pueden seleccionar de un menú desplegable.
- El filtro de productos permite buscar por marca y categoría.
- Se utiliza un sistema de autenticación y autorización para asegurar que solo los usuarios administradores puedan acceder a ciertas vistas.
- La API permite interactuar con los productos de manera programática utilizando solicitudes HTTP estándar.


