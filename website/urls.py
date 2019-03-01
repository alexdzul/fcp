from django.urls import path
from . import views



urlpatterns = {
    path('<int:product_id>/', views.detail, name='detail'),
    path('', views.Index.as_view(), name='index'),
    path('contacto/', views.ContactView.as_view(), name='contacto'),
    path('quienes-somos/', views.Quienes.as_view(), name='quienes'),
    path('nuestra-historia/', views.Historia.as_view(), name='historia')
}
