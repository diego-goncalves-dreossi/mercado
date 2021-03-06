from django.db import models
from autenticacao.models import Usuario
from fornecedores.models import Fornecedor
from produtos.models import Produto


class Pedido(models.Model):
    escolhas_pag = (
        ('Cr','Crédito',),
        ('De','Débito',),
        ('Di','Dinheiro',),
        ('Cp','Criptomoeda',),
    )

    status_opc = (
        ('Ac','A caminho'),
        ('Ev','Enviado'),
        ('En','Entregue'),
        ('At','Atrasado'),
        ('Ca','Cancelado'),
    )
    
    produto = models.ForeignKey(Produto,on_delete=models.DO_NOTHING)
    filial = models.CharField(max_length=200)
    pagamento = models.CharField(max_length=20,choices=escolhas_pag)
    qntnovosprods = models.IntegerField(default=1)
    status = models.CharField(max_length=20,choices=status_opc)
    usuario = models.ForeignKey(Usuario,on_delete=models.DO_NOTHING,default=1)

    def __str__(self):   
        return f'Pedido {self.id}'