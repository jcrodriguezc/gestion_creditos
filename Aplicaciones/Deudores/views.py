from django.shortcuts import redirect, render, redirect
from .models import Cliente

# Create your views here.

def home(request):
    clientes = Cliente.objects.all()
    return render(request,"gestionCreditos.html",{"clientes":clientes})

def registrarCliente(request):
    identificacion = request.POST['numIdentificacion']
    nombre = request.POST['txtNombre']
    credito = request.POST['numCredito']
    valor = request.POST['numValor']
    plazo = request.POST['numPlazo']
    cuota = request.POST['numCuota']

    cliente = Cliente.objects.create(
        identificacion=identificacion, nombre=nombre, idCredito=credito, valor=valor, plazo=plazo, cuota=cuota)

    return redirect('/')

def editarCliente(request,identificacion):
    cliente = Cliente.objects.get(identificacion=identificacion)
    return render(request, "editarCliente.html",{"cliente":cliente})

def edicionCliente(request):
    identificacion = request.POST['numIdentificacion']
    nombre = request.POST['txtNombre']
    credito = request.POST['numCredito']
    valor = request.POST['numValor']
    plazo = request.POST['numPlazo']
    cuota = request.POST['numCuota']

    cliente = Cliente.objects.get(identificacion=identificacion)        
    cliente.nombre = nombre
    cliente.idCredito = credito
    cliente.valor = valor
    cliente.plazo = plazo
    cliente.cuota = cuota
    cliente.save()
    return redirect('/')


def eliminarCliente(request,identificacion):
    curso = Cliente.objects.get(identificacion=identificacion)
    curso.delete()
    return redirect('/')