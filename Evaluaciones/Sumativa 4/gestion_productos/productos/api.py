from ninja import NinjaAPI, Schema
from django.shortcuts import get_object_or_404
from .models import Producto, Marca, Categoria, Caracteristica
from .schemas import ProductoSchema
from ninja.security import HttpBearer
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.contrib.auth import authenticate
from django.http import Http404, JsonResponse
from .utils import generar_token, JWTAuth
from pydantic import ValidationError


# Inicializar API
api = NinjaAPI(
    title="API de Productos",
    version="1.0.0",
    description="API para gestionar productos  de una tienda",
)

# Crea el objeto auth
auth = JWTAuth()

# Manejadores de Errores
@api.exception_handler(Http404)
def error_404(request, ex):
    return api.create_response(request, 
                               {'response': 'Recurso no encontrado'},
                               status=404)
    
@api.exception_handler(ValidationError)
def error_validacion(request, ex):
    return api.create_response(request,
                               {
                                   'response': 'Error de Formato de Entrada',
                                   'errores': ex.errors()
                               },
                               status=422)

# Servicios de la API

# Esquema para la autenticación
class AuthRequest(Schema):
    username: str
    password: str

# **Servicio: Obtener Token JWT**
# **Método:** POST
# **Descripción:** Permite obtener un token JWT para el usuario autenticado.
# **Entradas:**
# - username: El nombre de usuario para la autenticación (string).
# - password: La contraseña del usuario (string).
# **Salidas:**
# - token: El token JWT generado (string).
# - error: Mensaje de error si las credenciales no son válidas.

@api.post("/token")
def get_token(request, data: AuthRequest):
    user = authenticate(username=data.username, password=data.password)
    if not user:
        return {"error": "Credenciales inválidas"}
    token = generar_token(user)
    return {"token": token}

# **Servicio: Listar Productos**
# **Método:** GET
# **Descripción:** Devuelve una lista de todos los productos disponibles.
# **Entradas:** No tiene parámetros de entrada.
# **Salidas:** Lista de productos con los campos: id, código, nombre, precio, marca y categoría.

@api.get("/productos/", auth=auth)
def listar_productos(request):
    productos = Producto.objects.all().values('id', 'codigo', 'nombre', 'precio', 'marca__nombre', 'categoria__nombre')
    return list(productos)

# **Servicio: Detalle de Producto**
# **Método:** GET
# **Descripción:** Devuelve los detalles de un producto específico dado su ID.
# **Entradas:**
# - producto_id: El ID del producto (entero).
# **Salidas:** Detalles del producto, incluyendo: id, código, nombre, precio, marca, categoría y características.

@api.get("/productos/{producto_id}", auth=auth)
def detalle_producto(request, producto_id: int):
    producto = get_object_or_404(Producto, id=producto_id)
    return {
        "id": producto.id,
        "codigo": producto.codigo,
        "nombre": producto.nombre,
        "precio": producto.precio,
        "marca": producto.marca.nombre,
        "categoria": producto.categoria.nombre,
        "caracteristicas": [c.nombre for c in producto.caracteristicas.all()]
    }

# **Servicio: Crear Producto**
# **Método:** POST
# **Descripción:** Permite crear un nuevo producto en el sistema.
# **Entradas:**
# - data: Datos del producto que se desea crear, incluyendo: código, nombre, precio, marca, categoría y características.
# **Salidas:** El producto creado con los detalles: id, código, nombre, precio, marca y categoría.

@api.post("/productos/", auth=auth)
def crear_producto(request, data: ProductoSchema):
    try:
        marca = get_object_or_404(Marca, id=data.marca_id)
        categoria = get_object_or_404(Categoria, id=data.categoria_id)
        caracteristicas = Caracteristica.objects.filter(id__in=data.caracteristicas_ids)

        producto = Producto.objects.create(
            codigo=data.codigo,
            nombre=data.nombre,
            precio=data.precio,
            marca=marca,
            categoria=categoria
        )
        producto.caracteristicas.set(caracteristicas)
        producto.save()

        return JsonResponse({
            "id": producto.id,
            "codigo": producto.codigo,
            "nombre": producto.nombre,
            "precio": producto.precio,
            "marca": producto.marca.nombre,
            "categoria": producto.categoria.nombre
        }, status=201)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)

# **Servicio: Eliminar Producto**
# **Método:** DELETE
# **Descripción:** Elimina un producto específico del sistema.
# **Entradas:**
# - producto_id: El ID del producto que se desea eliminar (entero).
# **Salidas:** Mensaje de éxito si el producto fue eliminado, o un mensaje de error en caso de fallar.

@api.delete("/productos/{producto_id}", auth=auth)
def eliminar_producto(request, producto_id: int):
    try:
        producto = get_object_or_404(Producto, id=producto_id)
        producto.delete()
        return JsonResponse({"success": f"Producto con ID {producto_id} eliminado"}, status=200)
    except Exception as e:
        return JsonResponse({"error": f"Error al eliminar producto: {str(e)}"}, status=400)
