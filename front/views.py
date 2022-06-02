from django.shortcuts import render

from front.models import Categoria

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
    return render(request, 'flores.html')

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

def producto2(request):
    return render(request, 'producto2.html')

def register(request):
    return render(request, 'register.html')

def testeo(request):
    return render(request, 'testeo.html')

def tierra(request):
    return render(request, 'tierra.html')

def quevendemos(request):
    categorias = Categoria.objects.all()
    datos = {
        'listaCategorias': categorias
    }
    return render(request, 'quevendemos.html', datos)