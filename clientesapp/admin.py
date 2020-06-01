from django.contrib import admin

from .models import Client, Endereco, Fornecedor, Phone

# Register your models here.
admin.site.register(Client)
admin.site.register(Endereco)
admin.site.register(Fornecedor)
admin.site.register(Phone)