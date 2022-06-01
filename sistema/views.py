from django.http import HttpResponse
from django.shortcuts import render

from autenticacao.models import Usuario
from .models import Categoria,Filial,Fornecedor,Pedido,Produto

def inicio(request):
    return render(request,'inicio.html',{'usuario_logado':request.session.get('usuario')})

def sobre(request):
    return render(request,'sobre.html',{'usuario_logado':request.session.get('usuario')})

def adProduto(request):
    
    return render(request,'produto/adproduto.html',{'usuario_logado':request.session.get('usuario')})



def listaProdutos(request):
    return render(request,'produto/produtos.html',{'usuario_logado':request.session.get('usuario')})

def listaFiliais(request):
    return render(request,'filial/filiais.html',{'usuario_logado':request.session.get('usuario')})

def listaFornecedores(request):
    return render(request,'fornecedor/fornecedores.html',{'usuario_logado':request.session.get('usuario')})