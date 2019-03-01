from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic


class Index(View):

    def get(self, request):
        return render(request, 'index.html')

class Quienes(View):
        def get(self, request):
            return render(request, 'quienessomos.html')