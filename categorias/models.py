from django.db import models
from autenticacao.models import Usuario

class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField()
    usuario = models.ForeignKey(Usuario,on_delete=models.DO_NOTHING)

    def __str__(self):   
        return self.nome

    # Bebidas, Hortifruti, Açougue, Limpeza, Padaria, Doces, Cereais e farináceos, Enlatados, Laticínios, Higiene Pessoal, Peixaria, Eletrônicos, Mercearia 

