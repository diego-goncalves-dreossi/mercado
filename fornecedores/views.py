from ast import Return
from django.http import HttpResponse
from django.shortcuts import redirect, render

from autenticacao.models import Usuario
from categorias.models import Categoria
from fornecedores.models import Fornecedor


"""
request.session.get('usuario'): Se usuário está logado 
request.method == 'POST': Se função foi alcançada atraves de um botão, não atraves de escrevendo na barra de pesquisa
request.session.get('usuario') == cat.usuario.id: Evita a falha de segurança de alguém poder mexer no sistema pelo inspecionar
"""
def adFornecedor(request):
    if request.session.get('usuario'):
        return render(request,'adFornecedor.html',{'usuario_logado':request.session.get('usuario')})

def adFornecedorBD(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id=request.session['usuario'])
        

        if request.method == 'POST':
            nfornecedor = request.POST.get('nfornecedor')
            cnpj = request.POST.get('cnpj')
            logo = request.FILES.get('id_imagem')

            if not nfornecedor or not cnpj:
                print('Campos vazios')
                return redirect('/fornecedores/adfornecedor',{'usuario_logado':request.session.get('usuario')})
                
            else:
                fn = Fornecedor(nome=nfornecedor,cnpj=cnpj,usuario=usuario)

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
        
def listaFornecedores(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id=request.session['usuario'])
        fncd = Fornecedor.objects.filter(usuario=usuario)
        #return HttpResponse('lISTA FORNECEDORES')
        return render(
            request,
            'fornecedores.html',
            {
                'usuario_logado':request.session.get('usuario'),
                'fncd':fncd
            }
        
        )

def verFornecedor(request,id):
    if request.session.get('usuario'):
        fn = Fornecedor.objects.get(id=id)
        # Evita a falha de segurança de alguém poder mexer no sistema pelo inspecionar
        if request.session.get('usuario') == fn.usuario.id: 
            return render(
                request,
                'verfornecedor.html',
                {
                    'usuario_logado':request.session.get('usuario'),
                    'fn':fn
                }
            )

def pageditarFornecedor(request,id):
        if request.session.get('usuario'):
            fn = Fornecedor.objects.get(id=id)
            # Evita a falha de segurança de alguém poder mexer no sistema pelo inspecionar
            if request.session.get('usuario') == fn.usuario.id: 
                return render(
                request,
                'editarfornecedor.html',
                {
                    'usuario_logado':request.session.get('usuario'),
                    'fn':fn
                }
            )

def edtFornecedorBD(request):
    if request.session.get('usuario'):
        fornecedor_id = request.POST.get('fornecedor_id')
        nfornecedor = request.POST.get('nfornecedor')
        cnpj = request.POST.get('cnpj')
        fn = Fornecedor.objects.get(id=fornecedor_id)
        print(fornecedor_id,nfornecedor,cnpj,fn)

        # Evita a falha de segurança de alguém poder mexer no sistema pelo inspecionar
        if fn.usuario.id == request.session['usuario'] and request.method == 'POST':
            try:
                #return HttpResponse('NÃO É NONE PORRA')
                fn.nome = nfornecedor
                fn.cnpj = cnpj
                fn.save()
                return redirect(
                    '/fornecedores/listafornecedores',
                    {
                        'usuario_logado':request.session.get('usuario'),
                        'fn':fn
                    }
                
                )
            except Exception as erro:
                print(erro)
                return HttpResponse('Erro ao editar fornecedor')

def excluirFornecedor(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id=request.session['usuario'])
        categoria_id = request.POST.get('categoria_id')
        ctgs = Categoria.objects.filter(usuario=usuario)
        ctg = Categoria.objects.get(id=categoria_id)
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
