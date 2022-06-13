from django.shortcuts import render

from front.models import *

# Create your views here.

def home(request):
    return render(request, 'index.html')

def arbustos(request):
    return render(request, 'arbustos.html')

def carrito(request):
    return render(request, 'carrito.html')

def catalogo(request):
    return render(request, 'catalogo.html')

def equipo(request):
    return render(request, 'equipo.html')

def flores(request):
    fotos = Foto.objects.all()
    datos ={'fotos': fotos} #par ordenado de atributo y valor que se van a pasar a la vista
    return render(request, 'flores.html', datos)

def geo(request):
    return render(request, 'geo.html')

def login(request):
    return render(request, 'login.html')

def maceteros(request):
    return render(request, 'maceteros.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def producto(request):
    return render(request, 'producto.html')

def margarita(request):
    return render(request, 'margarita.html')

def register(request):
    return render(request, 'register.html')

def testeo(request):
    return render(request, 'testeo.html')

def tierra(request):
    return render(request, 'tierra.html')

def quevendemos(request):
    cat = Categoria.objects.all()
    contexto = {'cat': cat}
    return render(request, 'quevendemos.html', contexto)

def verproductos(request, id):
    cats = Categoria.objects.get(idCategoria = id)
    prods = Producto.objects.filter(categoria = cats)
    contexto = {'cat': cats, 'prods': prods}
    return render(request, 'verproductos.html', contexto)

def categorias(request):
    cat = Categoria.objects.all()
    contexto = {'cat': cat}
    return render(request, 'categorias.html', contexto)

def leerCategoria(request, id):
    cats = Categoria.objects.get(idCategoria = id)
    prods = Producto.objects.filter(categoria = cats)
    contexto = {'cat': cats, 'prods': prods}
    return render(request, 'leercategorias.html', contexto)