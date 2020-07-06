from django.contrib import admin

from .models import Client, Endereco, Phone

# Register your models here.
admin.site.register(Client)
admin.site.register(Endereco)
admin.site.register(Phone)