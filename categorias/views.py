from ast import Return
from django.http import HttpResponse
from django.shortcuts import redirect, render

from autenticacao.models import Usuario
from .models import Categoria


"""
request.session.get('usuario'): Se usuário está logado 
request.method == 'POST': Se função foi alcançada atraves de um botão, não atraves de escrevendo na barra de pesquisa
request.session.get('usuario') == cat.usuario.id: Evita a falha de segurança de alguém poder mexer no sistema pelo inspecionar
"""
def adCategoria(request):
    if request.session.get('usuario'):
        return render(request,'adcategoria.html',{'usuario_logado':request.session.get('usuario')})

def adCategoriasBD(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id=request.session['usuario'])
        ctgs = Categoria.objects.filter(usuario=usuario)
        if request.method == 'POST':
            nome_setor = request.POST.get('ncategoria')
            descricao_setor = request.POST.get('dcategoria')

            if not nome_setor or not descricao_setor:
                print('Campos vazios')
                return redirect('/categorias/adcategoria',{'usuario_logado':request.session.get('usuario')})
                
            else:
                setor = Categoria(nome=nome_setor,descricao=descricao_setor,usuario=usuario)

            try:
                setor.save()
                print('Categoria salva')
                return redirect(
                    '/categorias/listacategorias',
                    {
                        'usuario_logado':request.session.get('usuario'),
                        'ctgs':ctgs
                    }
                
                )
            except Exception as erro:
                print(erro)
                return HttpResponse('Erro ao salvar categoria')
        
def listaCategoria(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id=request.session['usuario'])
        ctgs = Categoria.objects.filter(usuario=usuario)
        return render(
            request,
            'categorias.html',
            {
                'usuario_logado':request.session.get('usuario'),
                'ctgs':ctgs
            }
        
        )

def verCategoria(request,id):
    if request.session.get('usuario'):
        ctg = Categoria.objects.get(id=id)
        # Evita a falha de segurança de alguém poder mexer no sistema pelo inspecionar
        if request.session.get('usuario') == ctg.usuario.id: 
            return render(
                request,
                'vercategoria.html',
                {
                    'usuario_logado':request.session.get('usuario'),
                    'cat':ctg
                }
            )

def pageditarCategoria(request,id):
        if request.session.get('usuario'):
            ctg = Categoria.objects.get(id=id)
            # Evita a falha de segurança de alguém poder mexer no sistema pelo inspecionar
            if request.session.get('usuario') == ctg.usuario.id: 
                return render(
                request,
                'editarcategoria.html',
                {
                    'usuario_logado':request.session.get('usuario'),
                    'cat':ctg
                }
            )

def edtCategoriaBD(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id=request.session['usuario'])
        categoria_id = request.POST.get('categoria_id')
        ncategoria = request.POST.get('ncategoria')
        dcategoria = request.POST.get('dcategoria')
        ctgs = Categoria.objects.filter(usuario=usuario)
        ctg = Categoria.objects.get(id=categoria_id)


        # Evita a falha de segurança de alguém poder mexer no sistema pelo inspecionar
        if ctg.usuario.id == request.session['usuario'] and request.method == 'POST':
            try:
                ctg.nome = ncategoria
                ctg.descricao = dcategoria
                ctg.save()
                return redirect(
                    '/categorias/listacategorias',
                    {
                        'usuario_logado':request.session.get('usuario'),
                        'ctgs':ctgs
                    }
                
                )
            except Exception as erro:
                print(erro)
                return HttpResponse('Erro ao editar categoria')

def excluirCategoria(request,id):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id=request.session['usuario'])
        ctgs = Categoria.objects.filter(usuario=usuario)
        ctg = Categoria.objects.get(id=id)
        # Evita a falha de segurança de alguém poder mexer no sistema pelo inspecionar
        if ctg.usuario.id == request.session['usuario']:
            try:
                ctg = ctg.delete()
                return redirect(
                    '/categorias/listacategorias',
                    {
                        'usuario_logado':request.session.get('usuario'),
                        'ctgs':ctgs
                    }
                
                )
            except Exception as erro:
                print(erro)
                return HttpResponse('Erro ao excluir categoria')
        else:
            print(request.method == 'POST')
            return HttpResponse('request.method')
