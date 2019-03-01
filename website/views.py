from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Whoweare,Contact,Ourhistory

class Index(View):

    def get(self, request):
        return render(request, 'index.html')

class ContactView(View):

    def get(self, request):
        return render(request, 'contacto.html')

    def post(self, request):
        email = request.POST['email']
        contact = Contact()
        contact.email= email
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

