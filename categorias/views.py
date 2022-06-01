from django.http import HttpResponse
from django.shortcuts import redirect, render

from autenticacao.models import Usuario
from .models import Categoria

def adCategoria(request):
    if request.session.get('usuario'):
        return render(request,'adcategoria.html',{'usuario_logado':request.session.get('usuario')})

def adCategoriasBD(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id=request.session['usuario'])
        ctgs = Categoria.objects.filter(usuario=usuario)
        if request.method == 'POST':
            nome_setor = request.POST.get('nsetor')
            descricao_setor = request.POST.get('dsetor')

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
    #livro = Livro.objects.get(id=id)
    if request.session.get('usuario'):
        pass
    return
