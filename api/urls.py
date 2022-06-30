from django.urls import path
from .views import *

urlpatterns= [
    path('traerProductos/', traerProductos, name='traer_productos'),
]