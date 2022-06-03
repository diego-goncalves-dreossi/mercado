from django.db import models
from autenticacao.models import Usuario
from categorias.models import Categoria
from fornecedores.models import Fornecedor


class Produto(models.Model):
    nome = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    preco = models.FloatField()
    descricao = models.TextField()
    usuario = models.ForeignKey(Usuario,on_delete=models.DO_NOTHING)
    img = models.ImageField(upload_to = 'produtos',null=True,blank=True)
    estoque = models.IntegerField(default=0)
    fornecedor = models.ForeignKey(Fornecedor,on_delete=models.DO_NOTHING)

    def __str__(self):   
        return self.nome
