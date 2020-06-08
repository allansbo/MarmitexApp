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