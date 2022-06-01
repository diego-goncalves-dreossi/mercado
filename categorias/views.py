from django.http import HttpResponse
from django.shortcuts import render

from autenticacao.models import Usuario
from .models import Categoria

def adCategoria(request):
    return render(request,'adcategoria.html',{'usuario_logado':request.session.get('usuario')})

def adCategoriasBD(request):
    if request.method == 'POST':
        nome_setor = request.POST.get('nsetor')
        descricao_setor = request.POST.get('dsetor')

        if not nome_setor or not descricao_setor:
            print('Campos vazios')
            return render(request,'adcategoria.html',{'usuario_logado':request.session.get('usuario')})
        else:
            setor = Categoria(nome=nome_setor,descricao=descricao_setor,usuario=request.session.get('usuario'))

        try:
            setor.save()
            print('Categoria salva')
            return render(request,'categorias.html',{'usuario_logado':request.session.get('usuario')})
        except Exception as erro:
            print(erro)
            return HttpResponse('Erro ao salvar categoria')
        

def listaCategoria(request):
    return render(request,'categorias.html',{'usuario_logado':request.session.get('usuario')})
