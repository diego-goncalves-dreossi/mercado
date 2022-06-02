from django.contrib import admin
from .models import Fornecedor

@admin.register(Fornecedor)
class UsuarioAdmin(admin.ModelAdmin):
    # Torna os dados dos usuários não mutáveis pelos administradores do sistema
    readonly_fields = ('nome','cnpj','usuario','img')
