from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Client, Endereco, Phone

class clientAddForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['client_name', 'client_email']
        labels = {
            'client_name': _('Nome completo'),
            'client_email': _('E-mail'),
        }


class phoneAddForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = ['id', 'phone_ddd', 'phone_number']
        labels = {
            'phone_ddd': _('DDD'),
            'phone_number': _('Número'),
        }


class enderecoAddForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ['id', 'endereco_cep', 'endereco_logradouro', 'endereco_complemento', 'endereco_numero', 'endereco_bairro', 'endereco_cidade', 'endereco_estado']
        labels = {
            'endereco_cep': _('CEP'),
            'endereco_logradouro': _('Logradouro'),
            'endereco_complemento': _('Complemento'),
            'endereco_numero': _('Número'),
            'endereco_bairro': _('Bairro'),
            'endereco_cidade': _('Cidade'),
            'endereco_estado': _('Estado')
        }