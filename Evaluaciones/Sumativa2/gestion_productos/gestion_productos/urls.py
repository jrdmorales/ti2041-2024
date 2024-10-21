from django.contrib import admin
from django.urls import path
from productos import views
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registro/', views.registro_producto, name='registro_producto'),
    path('resultado/', views.resultado_producto, name='resultado_producto'),
    path('consulta/', views.consulta_productos, name='consulta_productos'),
    path('filtrar/', views.filtrar_productos, name='filtrar_productos'),
    path('listar/', views.listar_productos, name='listar_productos'),
    path('productos/', views.inicio, name='inicio'),
    path('', lambda request: redirect('productos/')),


]
