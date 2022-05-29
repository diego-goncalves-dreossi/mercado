from django.db import models
from autenticacao.models import Usuario

class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField()
    usuario = models.ForeignKey(Usuario,on_delete=models.DO_NOTHING)

    def __str__(self):   
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    preco = models.FloatField()
    descricao = models.TextField()
    usuario = models.ForeignKey(Usuario,on_delete=models.DO_NOTHING)

    def __str__(self):   
        return self.nome

class Mercado(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)
    usuario = models.ForeignKey(Usuario,on_delete=models.DO_NOTHING)

    def __str__(self):   
        return self.nome

class FormaPagamento(models.Model):
    forma = models.CharField(max_length=50)
    idcartao = models.CharField(max_length=50)

    def __str__(self):   
        return f"{self.nome} {self.idcartao}"