from django.shortcuts import render
from django.views.generic import View
from sales.models import Product
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Whoweare, Contact,Ourhistory




class Index(View):

    def get(self, request):
        return render(request, 'index.html')

class ContactView(View):

    def get(self, request):
        return render(request, 'contacto.html')

    def post(self, request):
        email = request.POST['email']
        comentario = request.POST['comentario']
        contact = Contact()
        contact.email = email
        contact.comentario = comentario
        contact.save()
        ctx = {
            'save': True
        }
        return render(request, 'contacto.html', ctx)

class Quienes(View):
        def get(self, request):
            who = Whoweare.objects.all().first()
            ctx = {'who':who}
            return render(request, 'quienessomos.html',ctx)

class Historia(View):
    def get(self, request):
        our = Ourhistory.objects.all().first()
        ctx = {'our': our}
        return render(request, 'nuestrahistoria.html', ctx)

def detail(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404("La pregunta no existe")
    ctx = {'detail': product}
    return render(request, 'detail.html', ctx)