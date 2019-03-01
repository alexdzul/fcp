from django.shortcuts import render
from .models import Products

# Create your views here.
def index(request):
    name = Products.objects.all()#Question es el nombre de la class del modelo, .object es para acceder a los "objetos", .all()todos
    contexto={
        'latest_products_list': name,
    }
    return render(request,'index.html',contexto)