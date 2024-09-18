from django.shortcuts import render, redirect
from .forms import ProductoForm

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


