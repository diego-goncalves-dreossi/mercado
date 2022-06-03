from django.contrib import admin
from .models import Pedido,Produto


@admin.register(Produto)
class UsuarioAdmin(admin.ModelAdmin):
    # Torna os dados dos usuários não mutáveis pelos administradores do sistema
    readonly_fields = ('nome','categoria','preco','descricao','usuario','img','estoque','fornecedor')
