from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import Client
from .forms import clientAddForm


# Create your views here.
def clientslist(request):
    listaclientes = Client.objects.all()
    return render(request, 'clientesapp/clientes.html', {'listaclientes': listaclientes})


def clientedit(request, id):
    editarcliente = get_object_or_404(Client, pk=id)
    form = clientAddForm(instance=editarcliente)

    if request.method == 'POST':
        form = clientAddForm(request.POST, instance=editarcliente)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'clientesapp/editar-cliente.html', {'form': form, 'editarcliente': editarcliente})
    else:
        return render(request, 'clientesapp/editar-cliente.html', {'form': form, 'editarcliente': editarcliente})


def clientadd(request):
    if request.method == 'POST':
        form = clientAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = clientAddForm()
        return render(request, 'clientesapp/adicionar-cliente.html', {'form': form})


def helloWorld(request):
    return HttpResponse('Hello World!')


def yourname(request, name):
    return render(request, 'clientesapp/yourname.html', {'name': name})
