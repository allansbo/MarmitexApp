from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def helloWorld(request):
    return HttpResponse('Hello World!')

def yourname(request, name):
    return render(request, 'clientesapp/yourname.html', {'name': name})

def clientslist(request):
    return render(request, 'clientesapp/clientes.html')