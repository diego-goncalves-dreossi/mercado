from django.http import HttpResponse, FileResponse, Http404
from django.shortcuts import redirect, render
from django.core import serializers
from autenticacao.models import Usuario
from pedidos.models import Pedido
from categorias.models import Categoria
import json
from zipfile import ZipFile
from shutil import make_archive


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

def gerarJSON(request):
    return render(request,'paginasjson/gerar.html',{'usuario_logado':request.session.get('usuario')})

def exportarCategorias(request):
    try:
        usuario = Usuario.objects.get(id=request.session['usuario'])
        dados = Categoria.objects.filter(usuario=usuario)
        dados = serializers.serialize('json',dados)
        #f = open('static/dados/categorias.json','w')
        #json.dump(dados,f, indent=4,sort_keys=True)
        #make_archive('static/dados/categorias.json', 'zip', 'static/dados/')

        with ZipFile('static/dados/categorias.zip','w') as arq:
            arq.write('static/dados/categorias.json')
        print('Funcionou converter/criar json')
        
        return redirect('/pagjson/pagexportar', {'usuario_logado':request.session.get('usuario'),'tabela':'Categorias'})
    except Exception as erro:
        print(erro)
        return redirect('/pagjson/pagexportar', {'usuario_logado':request.session.get('usuario')})

def exportarFornecedores(request):
    pass

def exportarProdutos(request):
    pass

def exportarPedidos(request):
    pass




