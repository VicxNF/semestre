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
from django.urls import path
from front.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('arbustos/', arbustos),
    path('carrito/', carrito),
    path('catalogo/', catalogo),
    path('equipo/', equipo),
    path('flores/', flores),
    path('geo/', geo),
    path('login/', login),
    path('maceteros/', maceteros),
    path('nosotros/', nosotros),
    path('producto/', producto),
    path('producto2/', producto2),
    path('register/', register),
    path('testeo/', testeo),
    path('tierra/', tierra),
    path('quevendemos/', quevendemos),
    path('verproductos/<codCategoria>', verproductos)
]
