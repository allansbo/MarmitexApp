from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
import datetime

from .models import Client, Phone, Endereco
from .forms import clientAddForm


# Create your views here.
@login_required()
def clientslist(request):
    totalclientes = Client.objects.count()
    totalclientestrintadias = Client.objects.filter(created_at__gt=datetime.datetime.now()-datetime.timedelta(days=30)).count()
    listaclientes = Client.objects.all()
    return render(request, 'clientesapp/clientes.html', {'listaclientes': listaclientes, 'totalclientes': totalclientes, 'totalclientestrintadias': totalclientestrintadias})


@login_required()
def clientedit(request, id):
    editarcliente = get_object_or_404(Client, pk=id)
    form = clientAddForm(instance=editarcliente)

    if request.method == 'POST':
        form = clientAddForm(request.POST, instance=editarcliente)
        if form.is_valid():
            form.save()
            messages.info(request, 'O registro foi atualizado com sucesso!')
            return redirect('/clientes')
        else:
            return render(request, 'clientesapp/editar-cliente.html', {'form': form, 'editarcliente': editarcliente})
    else:
        return render(request, 'clientesapp/editar-cliente.html', {'form': form, 'editarcliente': editarcliente})


@login_required()
def clientdelete(request, id):
    deletarcliente = get_object_or_404(Client, pk=id)
    deletarcliente.delete()
    messages.info(request, 'O registro foi excluído com sucesso!')
    return redirect('/clientes')

@login_required()
def clientview(request, id):
    vercliente = get_object_or_404(Client, pk=id)
    return render(request, 'clientesapp/ver-cliente.html', {'vercliente': vercliente})


@login_required()
def clientadd(request):
    if request.method == 'POST':
        novocliente = Client()
        novotelefone = Phone()
        novoendereco = Endereco()
        form = clientAddForm(request.POST)
        novocliente.client_name = form.cleaned_data["nome"]
        novocliente.client_email = form.cleaned_data["email"]
        if novocliente.is_valid():
            salvar = novocliente.save(commit=false)
            id = novocliente.id
            novotelefone.id = id
            novotelefone.phone_ddd = form.cleaned_data["ddd"]
            novotelefone.phone_number = form.cleaned_data["telefone"]
            novoendereco.id = id
            novoendereco.endereco_cep = form.cleaned_data["cep"]
            novoendereco.endereco_logradouro = form.cleaned_data["logradouro"]
            novoendereco.endereco_complemento = form.cleaned_data["complemento"]
            novoendereco.endereco_numero = form.cleaned_data["numero"]
            novoendereco.endereco_bairro = form.cleaned_data["bairro"]
            novoendereco.endereco_cidade = form.cleaned_data["cidade"]
            novoendereco.endereco_estado = form.cleaned_data["estado"]
            salvar.save()
            messages.info(request, 'O registro foi inserido com sucesso!')
            return redirect('/clientes')
    else:
        form = clientAddForm()
        return render(request, 'clientesapp/adicionar-cliente.html', {'form': form})


@login_required()
def helloWorld(request):
    return HttpResponse('Hello World!')


@login_required()
def yourname(request, name):
    return render(request, 'clientesapp/yourname.html', {'name': name})

@login_required()
def caixa(request):
    return render(request, 'clientesapp/caixa.html')

@login_required()
def dashboard(request):
    return render(request, 'clientesapp/dashboard.html')

@login_required()
def produto(request):
    return render(request, 'clientesapp/produto.html')

@login_required()
def produto_adicionar(request):
    return render(request, 'clientesapp/produto-adicionar.html')

@login_required()
def pedido(request):
    return render(request, 'clientesapp/pedido.html')

@login_required()
def pedido_adicionar(request):
    return render(request, 'clientesapp/pedido-adicionar.html')
