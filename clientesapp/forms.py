from django import forms

from .models import Client


class clientAddForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('client_name', 'client_email')
