from django.http import HttpResponse
from django.shortcuts import render

from autenticacao.models import Usuario
from pedidos.models import Pedido

def inicio(request):
    if request.session.get('usuario'):
        return render(request,'inicio.html',{'usuario_logado':request.session.get('usuario')})

def sobre(request):
    if request.session.get('usuario'):
        return render(request,'sobre.html',{'usuario_logado':request.session.get('usuario')})

