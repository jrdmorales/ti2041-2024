from django.contrib import admin
from django.urls import path
from productos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registro/', views.registro_producto, name='registro_producto'),
    path('resultado/', views.resultado_producto, name='resultado_producto'),
    path('consulta/', views.consulta_productos, name='consulta_productos'),
    path('', views.inicio, name='inicio'),
]
