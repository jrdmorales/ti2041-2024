from django import forms

class ProductoForm(forms.Form):
    codigo = forms.CharField(max_length=100)
    nombre = forms.CharField(max_length=100)
    marca = forms.CharField(max_length=100)
    fecha_vencimiento = forms.DateField(widget=forms.SelectDateWidget)
