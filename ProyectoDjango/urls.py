"""ProyectoDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api.views import ProductoViewSet
from front.views import *
from back.views import *
from api.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

router = routers.DefaultRouter()
router.register('productos', ProductoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name="home"),
    path('arbustos/', arbustos, name="arbustos"),
    path('carrito/', carrito, name="carrito"),
    path('catalogo/', catalogo, name="catalogo"),
    path('equipo/', equipo, name="equipo"),
    path('flores/', flores, name="flores"),
    path('geo/', geo, name="geo"),
    path('login/', login, name="login"),
    path('maceteros/', maceteros, name="maceteros"),
    path('nosotros/', nosotros, name="nosotros"),
    path('producto/', producto, name="producto"),
    path('margarita/', margarita, name="margarita"),
    path('register/', register, name="register"),
    path('testeo/', testeo, name="testeo"),
    path('tierra/', tierra, name="tierra"),
    path('productosapi/', productosApi, name="productosapi"),
    path('quevendemos/', quevendemos, name="quevendemos"),
    path('quevendemos/<int:id>', verproductos, name="verproductos"),
    path('logindjango/', logindjango, name="logindjango"),
    path('indexdjango/', indexdjango, name="indexdjango"),
    path('validarUsuario/', validarUsuario, name="validarusuario"),
    path('categorias/', categorias, name="categorias"),
    path('categorias/<int:id>', leerCategoria, name="leercategorias"),
    path('api/', include(router.urls), name="api"),
    path('', mantenedor, name="mantenedor"),
    path('listar/', listarProductos, name="listar"),
    path('modificar/<id>/', modificarProducto, name="modificar"),
    path('eliminar/<id>/', eliminarProducto, name="eliminar"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)