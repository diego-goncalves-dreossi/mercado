from django.contrib import admin
from .models import Categoria

@admin.register(Categoria)
class UsuarioAdmin(admin.ModelAdmin):
    # Torna os dados dos usuários não mutáveis pelos administradores do sistema
    readonly_fields = ('nome','descricao','usuario')
