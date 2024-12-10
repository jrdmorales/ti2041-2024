from django.contrib import admin
from django.urls import path
from productos import views
from productos.api import api  # Asegúrate de importar correctamente el objeto 'api'

urlpatterns = [
    # Ruta para la vista de login
    path('', views.login_view, name='login'),
    
    # Ruta para la vista del panel de administración de Django
    path('admin/', admin.site.urls),
    
    # Rutas para las vistas de productos
    path('api/', api.urls),  # Rutas de la API definidas con Django Ninja

    # Otras vistas no relacionadas con la API
    path('registro/', views.registro_producto, name='registro_producto'),
    path('filtrar/', views.filtrar_producto, name='filtrar_producto'),
    path('listar/', views.listar_producto, name='listar_producto'),
    path('resultado/', views.resultado_producto, name='resultado_producto'),
    path('productos/', views.inicio, name='inicio'),
    path('logout/', views.logout_view, name='logout'),
]
