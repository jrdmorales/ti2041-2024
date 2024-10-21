from django.shortcuts import render, redirect
from .forms import ProductoForm
from .models import Producto, Marca, Categoria, Caracteristica

# Vista para la página de inicio
def inicio(request):
    return render(request, 'inicio.html')

# Lista para almacenar productos temporalmente en memoria
productos_registrados = []

# Vistas para el registro y consulta de productos
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
def resultado_producto(request):
    if len(productos_registrados) == 0:
        # Si no hay productos registrados, redirigir a una página con un mensaje
        return render(request, 'resultado.html', {'producto': None, 'mensaje': 'No hay productos registrados.'})
    
    # Si hay productos, mostrar el último registrado
    return render(request, 'resultado.html', {'producto': productos_registrados[-1]})

# Vista para mostrar todos los productos registrados
def consulta_productos(request):
    return render(request, 'consulta.html', {'productos': productos_registrados})

# Vistas para agregar y listar productos
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
def listar_productos(request):
    return render(request, 'listar.html', {'productos': productos_registrados})


def filtrar_productos(request):
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
