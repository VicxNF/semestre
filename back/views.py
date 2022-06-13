from urllib import response
from django.http import HttpResponse
from django.shortcuts import render, redirect
from back.models import Usuario

# Create your views here.
def logindjango(request):
    return render(request, 'logindjango.html')

def validarUsuario(request):
    #recibimos los datos desde el formulario que fueron 
    #pasados via POST
    v_email=request.POST.get('email')
    v_password=request.POST.get('password')

    try:
    #Buscamos el usuario en la base de datos
        usu=Usuario.objects.get(email=v_email, password=v_password)

        if usu:
            request.session['usuario'] = v_email
            return redirect('/indexdjango/')

    except:
        return redirect('/logindjango/')



def indexdjango(request):
    if 'usuario' not in request.session:
        return redirect('/logindjango/')

    return render(request, 'indexdjango.html')