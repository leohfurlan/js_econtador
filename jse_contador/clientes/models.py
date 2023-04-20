from django.db import models

class Cliente(models.Model):
    cnpj = models.CharField(max_length=14)
    razao_social = models.CharField(max_length=200)
    nome_cliente = models.CharField(max_length=200)
    telefone = models.CharField(max_length=11)
    email = models.EmailField()
    