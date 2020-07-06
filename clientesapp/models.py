from django.db import models


# Create your models here.
class Phone(models.Model):
    phone_ddd = models.CharField(max_length=3)
    phone_number = models.CharField(max_length=10)


class Endereco(models.Model):
    ESTADOS = (
        ('', '- Escolha -'),
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
    endereco_cep = models.IntegerField()
    endereco_logradouro = models.CharField(max_length=255)
    endereco_complemento = models.CharField(max_length=128)
    endereco_numero = models.IntegerField()
    endereco_bairro = models.CharField(max_length=255)
    endereco_cidade = models.CharField(max_length=255)
    endereco_estado = models.CharField(choices=ESTADOS, max_length=2)



class Client(models.Model):
    client_name = models.CharField(max_length=150)
    client_email = models.EmailField()
    client_phone = models.ForeignKey('Phone', on_delete=models.CASCADE)
    client_endereco = models.ForeignKey('Endereco', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.client_name


class Fornecedor(models.Model):
    fornecedor_nome_empresa = models.CharField(max_length=255)
    fornecedor_cnpj = models.CharField(max_length=14)
    fornecedor_email = models.EmailField()
    fornecedor_site = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fornecedor_nome_empresa
