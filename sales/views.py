from django.shortcuts import render

# Create your views here.
def vista_producto(request):
    return render(request,'index.html')