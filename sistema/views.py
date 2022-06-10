from django.http import HttpResponse, FileResponse, Http404
from django.shortcuts import redirect, render
from django.core import serializers
from autenticacao.models import Usuario
from pedidos.models import Pedido
from categorias.models import Categoria
from fornecedores.models import Fornecedor
from produtos.models import Produto
import json
from zipfile import ZipFile
from shutil import make_archive


def inicio(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id=request.session['usuario'])
        peds = Pedido.objects.filter(usuario=usuario).order_by('-id')
        prods = Produto.objects.filter(usuario=usuario).order_by('-id')
        forns = Fornecedor.objects.filter(usuario=usuario).order_by('-id')

        if len(peds) < 6:
            peds = Pedido.objects.filter(usuario=usuario).order_by('-id')[:len(peds)]
        else:
            peds = Pedido.objects.filter(usuario=usuario).order_by('-id')[:6]

        if len(prods) < 6:
            prods = Produto.objects.filter(usuario=usuario).order_by('-id')[:len(prods)]
        else:
            prods = Produto.objects.filter(usuario=usuario).order_by('-id')[:6]
        
        
        if len(forns) < 6:
            forns = Fornecedor.objects.filter(usuario=usuario).order_by('-id')[:len(prods)]
        else:
            forns = Fornecedor.objects.filter(usuario=usuario).order_by('-id')[:6]
        
        
       
        return render(request,'inicio.html',{'usuario_logado':request.session.get('usuario'),'pedidos':peds,'produtos':prods,'fornecedores':forns})

def sobre(request):
    if request.session.get('usuario'):
        return render(request,'sobre.html',{'usuario_logado':request.session.get('usuario')})

def pagJSON(request):
    return render(request,'paginasjson/pagjson.html',{'usuario_logado':request.session.get('usuario')})

def pagJSONExp(request):
    
    return render(request,'paginasjson/pagexportar.html',{'usuario_logado':request.session.get('usuario')})

def gerarJSON(request):
    return render(request,'paginasjson/gerar.html',{'usuario_logado':request.session.get('usuario')})

def exportarCategorias(request):
    try:
        usuario = Usuario.objects.get(id=request.session['usuario'])
        dados = Categoria.objects.filter(usuario=usuario)
        dados = serializers.serialize('json',dados)
        f = open('static/dados/categorias.json','w')
        json.dump(dados,f, indent=4,sort_keys=True)
        make_archive('static/dados/categorias', 'zip', 'static/dados/')


        print('Categorias')
        return render(request,'paginasjson/pagexportar.html', {'usuario_logado':request.session.get('usuario'),'tabela':'Categorias'})
    except Exception as erro:
        print(erro)
        return render(request,'paginasjson/pagexportar.html', {'usuario_logado':request.session.get('usuario'),'tabela':'Categorias'})

def exportarFornecedores(request):
    try:
        usuario = Usuario.objects.get(id=request.session['usuario'])
        dados = Fornecedor.objects.filter(usuario=usuario)
        dados = serializers.serialize('json',dados)
        f = open('static/dados/fornecedores.json','w')
        json.dump(dados,f, indent=4,sort_keys=True)
        make_archive('static/dados/fornecedores', 'zip', 'static/dados/')
        print('Fornecedores')
        
        
        return render(request,'paginasjson/pagexportar.html', {'usuario_logado':request.session.get('usuario'),'tabela':'Fornecedores'})
    except Exception as erro:
        print(erro)
        return render(request,'paginasjson/pagexportar.html', {'usuario_logado':request.session.get('usuario'),'tabela':'Fornecedores'})

def exportarProdutos(request):
    try:
        usuario = Usuario.objects.get(id=request.session['usuario'])
        dados = Produto.objects.filter(usuario=usuario)
        dados = serializers.serialize('json',dados)
        f = open('static/dados/produtos.json','w')
        json.dump(dados,f, indent=4,sort_keys=True)
        make_archive('static/dados/produtos', 'zip', 'static/dados/')
        
        
        print('Produtos')
        return render(request,'paginasjson/pagexportar.html', {'usuario_logado':request.session.get('usuario'),'tabela':'Produtos'})
    except Exception as erro:
        print(erro)
        return render(request,'paginasjson/pagexportar.html', {'usuario_logado':request.session.get('usuario'),'tabela':'Produtos'})

def exportarPedidos(request):
    try:
        usuario = Usuario.objects.get(id=request.session['usuario'])
        dados = Pedido.objects.filter(usuario=usuario)
        dados = serializers.serialize('json',dados)
        f = open('static/dados/pedidos.json','w')
        json.dump(dados,f, indent=4,sort_keys=True)
        make_archive('static/dados/pedidos', 'zip', 'static/dados/')

        
        print('Pedidos')
        return render(request,'paginasjson/pagexportar.html', {'usuario_logado':request.session.get('usuario'),'tabela':'Pedidos'})
    except Exception as erro:
        print(erro)
        return render(request,'paginasjson/pagexportar.html', {'usuario_logado':request.session.get('usuario'),'tabela':'Pedidos'})




