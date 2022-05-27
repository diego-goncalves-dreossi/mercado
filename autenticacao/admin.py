from django.contrib import admin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    # Torna os dados dos usuários não mutáveis pelos administradores do sistema
    readonly_fields = ('nome','email','senha')

