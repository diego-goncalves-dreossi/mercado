from django.http import HttpResponse
from django.shortcuts import render

from autenticacao.models import Usuario
from .models import Categoria,Fornecedor,Pedido,Produto

def inicio(request):
    if request.session.get('usuario'):
        return render(request,'inicio.html',{'usuario_logado':request.session.get('usuario')})

def sobre(request):
    if request.session.get('usuario'):
        return render(request,'sobre.html',{'usuario_logado':request.session.get('usuario')})

def adProduto(request):
    if request.session.get('usuario'):
        return render(request,'produto/adproduto.html',{'usuario_logado':request.session.get('usuario')})



def listaProdutos(request):
    if request.session.get('usuario'):
        return render(request,'produto/produtos.html',{'usuario_logado':request.session.get('usuario')})

def listaFiliais(request):
    if request.session.get('usuario'):
        return render(request,'filial/filiais.html',{'usuario_logado':request.session.get('usuario')})

def listaFornecedores(request):
    if request.session.get('usuario'):
        return render(request,'fornecedor/fornecedores.html',{'usuario_logado':request.session.get('usuario')})