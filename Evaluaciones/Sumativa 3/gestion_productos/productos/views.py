
from .forms import ProductoForm
from .models import Producto, Marca, Categoria, Caracteristica
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Lista para almacenar productos temporalmente en memoria
productos_registrados = []

# Vista para Login
def login_view(request):
    # Evitar redirección al login si el usuario ya está autenticado
    if request.user.is_authenticated:
        return redirect('inicio')  # Cambia 'inicio' por la página principal de tu aplicación

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
# Vista para la página de inicio
@login_required
def inicio(request):
    return render(request, 'inicio.html')

# Vistas para el registro y consulta de productos
@login_required
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

# Vista para mostrar el último producto registrado
@login_required
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

# Vistas para agregar y listar productos
@login_required
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm()
    return render(request, 'registro', {'form': form})

# Vista para listar productos
@login_required
def listar_producto(request):
    return render(request, 'listar.html', {'productos': productos_registrados})

# Vistas para filtrar productos
@login_required
def filtrar_producto(request):
    # Inicializar productos con todos los productos registrados
    productos = productos_registrados

    # Obtener los valores de marca, categoría y característica desde el formulario de filtrado
    marca = request.GET.get('marca')
    categoria = request.GET.get('categoria')
    caracteristica = request.GET.get('caracteristica')

    # Aplicar los filtros si existen
    if marca:
        productos = [producto for producto in productos if producto['marca'].id == int(marca)]
    if categoria:
        productos = [producto for producto in productos if producto['categoria'].id == int(categoria)]
    if caracteristica:
        productos = [producto for producto in productos if caracteristica in producto['caracteristicas']]

    # Obtener todas las marcas, categorías y características para el formulario de filtro
    marcas = Marca.objects.all()
    categorias = Categoria.objects.all()
    caracteristicas = Caracteristica.objects.all()

    return render(request, 'filtrar.html', {
        'productos': productos,
        'marcas': marcas,
        'categorias': categorias,
        'caracteristicas': caracteristicas
    })