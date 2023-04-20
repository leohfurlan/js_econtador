from django.db import models
from django.forms import ModelForm
from clientes.models import Cliente

cliente_choices = Cliente.objects.values_list('id', 'razao_social')

class Documento(models.Model):
    cliente = models.IntegerField(verbose_name='Clientes', choices=cliente_choices, blank=True)
    nome_documento = models.CharField(max_length=50)
    arquivo = models.FileField(upload_to='documentos/anexos/')
    def __str__(self) -> str:
        return self.nome_documento