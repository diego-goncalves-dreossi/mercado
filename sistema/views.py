from django.http import HttpResponse, FileResponse, Http404
from django.shortcuts import redirect, render
from django.core import serializers
from autenticacao.models import Usuario
from pedidos.models import Pedido
from categorias.models import Categoria
import json
import zipfile as z

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
        objeto_json = json.dumps(dados, indent=4)
        with open("./media/dados/categorias.json", "w") as saida: 
            saida.write(objeto_json) 
        print('Funcionou')

        #x = open("./media/dados/categorias.json", "r")
        #print(x.read())

        #zipar
        arqz = z.ZipFile('./media/zipados/categorias.zip', 'w', z.ZIP_DEFLATED)
        arqz.write(filename="./media/dados/categorias.json")
        arqz.close()

        # Baixar
        nomearq = './media/zipados/categorias.zip'.split('./')[-1]
        resposta = FileResponse(open(nomearq,' rb'),as_attachment=True)
        return resposta
        return redirect('/inicio', {'usuario_logado':request.session.get('usuario')})
    except Exception as erro:
        print(erro)
        return redirect('/inicio', {'usuario_logado':request.session.get('usuario')})

def exportarFornecedores(request):
    pass

def exportarProdutos(request):
    pass

def exportarPedidos(request):
    pass




