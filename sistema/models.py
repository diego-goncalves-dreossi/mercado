from django.db import models
from autenticacao.models import Usuario
from fornecedores.models import Fornecedor
from produtos.models import Produto


class Pedido(models.Model):
    produto = models.ForeignKey(Produto,on_delete=models.DO_NOTHING)
    categoria = models.CharField(max_length=200,null=True,blank=True)
    fornecedor = models.ForeignKey(Fornecedor,on_delete=models.DO_NOTHING)
    filial = models.CharField(max_length=200)
    pagamento = models.CharField(max_length=20)
    qntnovosprods = models.IntegerField(default=1)
    usuario = models.ForeignKey(Usuario,on_delete=models.DO_NOTHING,default=1)

    def __str__(self):   
        return f'Pedido {self.nome}'