from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.core import serializers
from autenticacao.models import Usuario
from pedidos.models import Pedido
from categorias.models import Categoria
import json

def inicio(request):
    if request.session.get('usuario'):
        return render(request,'inicio.html',{'usuario_logado':request.session.get('usuario')})

def sobre(request):
    if request.session.get('usuario'):
        return render(request,'sobre.html',{'usuario_logado':request.session.get('usuario')})

def pagJSON(request):
    return render(request,'paginasjson/pagjson.html',{'usuario_logado':request.session.get('usuario')})

def pagJSONExp(request):
    return render(request,'paginasjson/pagexportar.html',{'usuario_logado':request.session.get('usuario')})

def exportarCategorias(request):
    try:
        usuario = Usuario.objects.get(id=request.session['usuario'])
        dados = Categoria.objects.filter(usuario=usuario)
        dados = serializers.serialize('json',dados)

        with open("/media/dados/categorias.json", "w") as saida: 
            json.dump(dados, saida) 
        pass
    except Exception as erro:
        print(erro)
        return redirect('/inicio', {'usuario_logado':request.session.get('usuario')})

def exportarFornecedores(request):
    pass

def exportarProdutos(request):
    pass

def exportarPedidos(request):
    pass




