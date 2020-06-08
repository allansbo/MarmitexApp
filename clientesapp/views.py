from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages

from .models import Client, Phone
from .forms import clientAddForm


# Create your views here.
@login_required()
def clientslist(request):
    listaclientes = Client.objects.all()
    listatelefone = Phone.objects.all()
    return render(request, 'clientesapp/clientes.html', {'listaclientes': listaclientes, 'listatelefone': listatelefone})


@login_required()
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


@login_required()
def clientdelete(request, id):
    deletarcliente = get_object_or_404(Client, pk=id)
    deletarcliente.delete()
    messages.info(request, 'O registro foi excluído com sucesso!')
    return redirect('/')


@login_required()
def clientadd(request):
    if request.method == 'POST':
        form = clientAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = clientAddForm()
        return render(request, 'clientesapp/adicionar-cliente.html', {'form': form})


@login_required()
def helloWorld(request):
    return HttpResponse('Hello World!')


@login_required()
def yourname(request, name):
    return render(request, 'clientesapp/yourname.html', {'name': name})
