from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarCliente/', views.registrarCliente),
    path('editarCliente/<identificacion>', views.editarCliente),
    path('edicionCliente/', views.edicionCliente),
    path('eliminarCliente/<identificacion>', views.eliminarCliente)
]