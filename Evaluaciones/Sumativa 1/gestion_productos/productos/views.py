from django.shortcuts import render, redirect
from .forms import ProductoForm

def inicio(request):
    return render(request, 'inicio.html')

# Lista para almacenar productos temporalmente en memoria
productos_registrados = []

def registro_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            productos_registrados.append(form.cleaned_data)
            return redirect('resultado_producto')
    else:
        form = ProductoForm()

    return render(request, 'registro.html', {'form': form})

def resultado_producto(request):
    return render(request, 'resultado.html', {'producto': productos_registrados[-1]})

def consulta_productos(request):
    return render(request, 'consulta.html', {'productos': productos_registrados})


