from django.db import models
from autenticacao.models import Usuario

class Fornecedor(models.Model):
    # Marcas
    nome = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=20)
    usuario = models.ForeignKey(Usuario,on_delete=models.DO_NOTHING)
    img = models.ImageField(upload_to = 'fornecedores',null=True,blank=True)

    def __str__(self):   
        return self.nome

