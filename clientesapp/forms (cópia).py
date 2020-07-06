from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django.utils.translation import ugettext_lazy as _

from .models import Client, Endereco, Phone

ESTADOS = (
    ('', 'Escolha'),
    ('AC', 'ACRE'),
    ('AL', 'ALAGOAS'),
    ('AP', 'AMAPÁ'),
    ('AM', 'AMAZONAS'),
    ('BA', 'BAHIA'),
    ('CE', 'CEARÁ'),
    ('DF', 'DISTRITO FEDERAL'),
    ('ES', 'ESPÍRITO SANTO'),
    ('GO', 'GOIÁS'),
    ('MA', 'MARANHÃO'),
    ('MT', 'MATO GROSSO'),
    ('MS', 'MATO GROSSO DO SUL'),
    ('MG', 'MINAS GERAIS'),
    ('PA', 'PARÁ'),
    ('PB', 'PARAÍBA'),
    ('PR', 'PARANÁ'),
    ('PE', 'PERNAMBUCO'),
    ('PI', 'PIAUÍ'),
    ('RJ', 'RIO DE JANEIRO'),
    ('RN', 'RIO GRANDE DO NORTE'),
    ('RS', 'RIO GRANDE DO SUL'),
    ('RO', 'RONDÔNIA'),
    ('RR', 'RORAIMA'),
    ('SC', 'SANTA CATARINA'),
    ('SP', 'SÃO PAULO'),
    ('SE', 'SERGIPE'),
    ('TO', 'TOCANTINS')
)

class clientAddForm(forms.Form):
    nome = forms.CharField(max_length=150)
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'exemplo@mail.com'}))
    ddd = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'DDD'}))
    telefone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Número com 9 digitos'}))
    cep = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Somente números'}))
    logradouro = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Rua, Avenida'}), max_length=255)
    complemento = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ap Bloco'}), max_length=128)
    numero = forms.IntegerField()
    bairro = forms.CharField(max_length=255)
    cidade = forms.CharField(max_length=255)
    estado = forms.ChoiceField(choices=ESTADOS)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('nome', css_class='form-group col-md-6 mb-0'),
                Column('email', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'logradouro',
            'complemento',
            Row(
                Column('cidade', css_class='form-group col-md-4 mb-0'),
                Column('estado', css_class='form-group col-md-3 mb-0'),
                Column('cep', css_class='form-group col-md-2 mb-0'),
                Column('ddd', css_class='form-group col-md-1 mb-0'),
                Column('telefone', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Cadastrar')
        )