
from .forms import ProductoForm
from .models import Producto, Marca, Categoria, Caracteristica
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, user_passes_test

# Lista para almacenar productos temporalmente en memoria
productos_registrados = []

# Comprobar si el usuario es administrador
def es_administrador(user):
    return user.is_staff

# Vista para Login
def login_view(request):
    # Evitar redirección al login si el usuario ya está autenticado
    if request.user.is_authenticated:
        return render(request, 'consulta.html', {'productos': productos_registrados})
    
    if request.user.is_staff:
        return redirect(reverse_lazy('inicio'))  # Cambia 'inicio' por la página principal de tu aplicación

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('inicio')  # Redirige a la página principal si el login es exitoso
        else:
            return render(request, 'login.html', {'error_message': 'Credenciales incorrectas.'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

# Vista para la página de inicio (solo para administradores)
@login_required
@user_passes_test(es_administrador)
def inicio(request):
    if not request.user.is_staff:
        return HttpResponseForbidden("Acceso denegado")
    return render(request, 'inicio.html')

# Vistas para el registro y consulta de productos
@login_required
@user_passes_test(es_administrador)
def registro_producto(request):
    # Si se envió un formulario, procesarlo
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        # Si el formulario es válido, agregar el producto a la lista y redirigir a la página de resultado
        if form.is_valid():
            productos_registrados.append(form.cleaned_data)
            return redirect('resultado_producto')
    else:
        form = ProductoForm()

    return render(request, 'registro.html', {'form': form})

# Vista para mostrar el último producto registrado (solo administradores)
@login_required
@user_passes_test(es_administrador)
def resultado_producto(request):
    if len(productos_registrados) == 0:
        # Si no hay productos registrados, redirigir a una página con un mensaje
        return render(request, 'resultado.html', {'producto': None, 'mensaje': 'No hay productos registrados.'})
    
    # Si hay productos, mostrar el último registrado
    return render(request, 'resultado.html', {'producto': productos_registrados[-1]})

# Vista para mostrar todos los productos registrados
@login_required
def consulta_producto(request):
    return render(request, 'consulta.html', {'productos': productos_registrados})


# Vista para listar productos
@login_required
def listar_producto(request):
    return render(request, 'listar.html', {'productos': productos_registrados})

# Vistas para filtrar productos
@login_required
def filtrar_producto(request):
    productos = Producto.objects.all()

    marca = request.GET.get('marca')
    categoria = request.GET.get('categoria')
    caracteristica = request.GET.get('caracteristica')

    if marca:
        productos = productos.filter(marca__id=marca)
    if categoria:
        productos = productos.filter(categoria__id=categoria)
    if caracteristica:
        productos = productos.filter(caracteristicas__id=caracteristica)

    marcas = Marca.objects.all()
    categorias = Categoria.objects.all()
    caracteristicas = Caracteristica.objects.all()

    return render(request, 'filtrar.html', {
        'productos': productos,
        'marcas': marcas,
        'categorias': categorias,
        'caracteristicas': caracteristicas
    })