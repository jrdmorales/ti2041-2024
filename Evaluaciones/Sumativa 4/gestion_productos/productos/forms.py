from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['codigo', 'nombre', 'precio', 'marca', 'categoria', 'caracteristicas']
        labels = {
            'codigo': 'Código del Producto',
            'nombre': 'Nombre del Producto',
            'precio': 'Precio',
            'marca': 'Marca Asociada',
            'categoria': 'Categoría Asociada',
            'caracteristicas': 'Características',
        }
        widgets = {
            'caracteristicas': forms.CheckboxSelectMultiple(),
        }
        help_texts = {
            'precio': 'Ingrese un valor mayor o igual a 0.',
        }

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio is not None and precio < 0:
            raise forms.ValidationError('El precio no puede ser negativo.')
        return precio

    def clean_codigo(self):
        codigo = self.cleaned_data.get('codigo')
        if not codigo.isalnum():
            raise forms.ValidationError('El código debe contener solo caracteres alfanuméricos.')
        return codigo
