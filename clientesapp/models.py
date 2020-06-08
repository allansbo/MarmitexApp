from django.db import models


# Create your models here.
class Client(models.Model):
    client_name = models.CharField(max_length=255)
    client_email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.client_name


class Phone(models.Model):
    phone_client = models.OneToOneField('Client', on_delete=models.CASCADE)
    phone_ddd = models.CharField(max_length=3)
    phone_number = models.CharField(max_length=10)
    phone_type = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Endereco(models.Model):
    endereco_cep = models.CharField(max_length=8)
    endereco_logradouro = models.CharField(max_length=255)
    endereco_complemento = models.CharField(max_length=128)
    endereco_numero = models.CharField(max_length=10)
    endereco_bairro = models.CharField(max_length=255)
    endereco_cidade = models.CharField(max_length=255)
    endereco_estado = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Fornecedor(models.Model):
    fornecedor_nome_empresa = models.CharField(max_length=255)
    fornecedor_cnpj = models.CharField(max_length=14)
    fornecedor_email = models.EmailField()
    fornecedor_site = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fornecedor_nome_empresa
