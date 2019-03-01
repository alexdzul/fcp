from django.urls import path
from . import views


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
#    path('contacto/', views.contact(), name='contacto')
    path('quienes-somos/', views.Quienes.as_view(), name='quienes'),
    ]
