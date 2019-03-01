from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):
    name = Product.objects.all()#Question es el nombre de la class del modelo, .object es para acceder a los "objetos", .all()todos
    contexto={
        'latest_product_list': name,
    }
    return render(request,'index.html',contexto)