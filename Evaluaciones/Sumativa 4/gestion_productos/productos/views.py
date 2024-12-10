from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Marca, Categoria
from .forms import ProductoForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required,user_passes_test
from productos.api import api

# Lista para almacenar productos temporalmente en memoria
productos_registrados = []


def es_administrador(user):
    return user.is_staff

# Vista para el inicio (listar productos)
@login_required
def inicio(request):
    productos = Producto.objects.all()
    return render(request, 'inicio.html', {'productos': productos})

# Vista para registrar un producto
@login_required
@user_passes_test(es_administrador)
def registro_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            productos_registrados.append(form.cleaned_data)
            return redirect('resultado_producto')
    else:
        form = ProductoForm()
    return render(request, 'registro.html', {'form': form})


# Vista para filtrar productos
@login_required
def filtrar_producto(request):
    # Obtener las categorías y marcas disponibles
    categorias = Categoria.objects.all()
    marcas = Marca.objects.all()

    # Obtener los parámetros de búsqueda de la URL
    categoria_id = request.GET.get('categoria')
    marca_id = request.GET.get('marca')

    # Filtrar productos según los parámetros de la URL
    productos = Producto.objects.all()

    if categoria_id:
        productos = productos.filter(categoria__id=categoria_id)
    if marca_id:
        productos = productos.filter(marca__id=marca_id)

    # Pasar los productos, categorías y marcas a la plantilla
    return render(request, 'filtrar.html', {
        'productos': productos,
        'categorias': categorias,
        'marcas': marcas,
        'categoria_seleccionada': categoria_id,
        'marca_seleccionada': marca_id,
    })

# Vista para listar todos los productos
@login_required
def listar_producto(request):
    productos = Producto.objects.all()
    return render(request, 'listar.html', {'productos': productos})

# Vistas para autenticación
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is None:
            return HttpResponse('Error de autenticación', status=401)
        if user:
            login(request, user)
            return redirect('inicio')
        else:
            return render(request, 'login.html', {'error': 'Credenciales incorrectas'})
    return render(request, 'login.html')

# Vista Resultado del registro
@login_required
@user_passes_test(es_administrador)
def resultado_producto(request):
    if len(productos_registrados) == 0:
        # Si no hay productos registrados, redirigir a una página con un mensaje
        return render(request, 'resultado.html', {'producto': None, 'mensaje': 'No hay productos registrados.'})
    
    # Si hay productos, mostrar el último registrado
    return render(request, 'resultado.html', {'producto': productos_registrados[-1]})

def logout_view(request):
    logout(request)
    return redirect('login')
