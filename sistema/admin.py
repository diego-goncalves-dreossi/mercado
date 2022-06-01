from django.contrib import admin
from .models import Categoria,Filial,Fornecedor,Pedido,Produto


@admin.register(Filial)
class UsuarioAdmin(admin.ModelAdmin):
    # Torna os dados dos usuários não mutáveis pelos administradores do sistema
    readonly_fields = ('nome','endereco','usuario','img')

@admin.register(Fornecedor)
class UsuarioAdmin(admin.ModelAdmin):
    # Torna os dados dos usuários não mutáveis pelos administradores do sistema
    readonly_fields = ('nome','cnpj','usuario','img')

@admin.register(Produto)
class UsuarioAdmin(admin.ModelAdmin):
    # Torna os dados dos usuários não mutáveis pelos administradores do sistema
    readonly_fields = ('nome','categoria','preco','descricao','usuario','img','estoque','fornecedor')
