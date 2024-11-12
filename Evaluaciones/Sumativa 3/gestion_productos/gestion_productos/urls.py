from django.contrib import admin
from django.urls import path
from productos import views
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registro/', views.registro_producto, name='registro_producto'),
    path('resultado/', views.resultado_producto, name='resultado_producto'),
    path('consulta/', views.consulta_producto, name='consulta_producto'),
    path('filtrar/', views.filtrar_producto, name='filtrar_producto'),
    path('listar/', views.listar_producto, name='listar_producto'),
    path('productos/', views.inicio, name='inicio'),
     path('', views.login_view, name='login'),
     path('logout/', views.logout_view, name='logout'),


]
