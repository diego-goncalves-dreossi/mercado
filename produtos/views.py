from ast import Return
from django.http import HttpResponse
from django.shortcuts import redirect, render
from os import remove
from autenticacao.models import Usuario
from categorias.models import Categoria
from fornecedores.models import Fornecedor
from produtos.models import Produto


"""
request.session.get('usuario'): Se usuário está logado 
request.method == 'POST': Se função foi alcançada atraves de um botão, não atraves de escrevendo na barra de pesquisa
request.session.get('usuario') == cat.usuario.id: Evita a falha de segurança de alguém poder mexer no sistema pelo inspecionar
"""
def adProduto(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id=request.session['usuario'])
        prods = Produto.objects.filter(usuario=usuario)
        fncd = Fornecedor.objects.filter(usuario=usuario)
        ctgs = Categoria.objects.filter(usuario=usuario)
        return render(
            request,
            'adproduto.html',
            {
                'usuario_logado':request.session.get('usuario'),
                'prods':prods,
                'fncd':fncd,
                'ctgs':ctgs
            }
        )

def adProdutoBD(request):
    if request.session.get('usuario'):
        
        if request.method == 'POST':
            usuario = Usuario.objects.get(id=request.session['usuario'])
            nprod = request.POST.get('nprod')
            c = request.POST.get('cat_prod')
            catp = Categoria.objects.get(id=c)
            preco = request.POST.get('pprod')
            foto = request.FILES['imageprod']
            desc = request.POST.get('dprod')
            est = request.POST.get('eprod')
            f = request.POST.get('forn_prod')
            fnp = Fornecedor.objects.get(id=f)
            
            try:
                if not nprod or not catp or not preco  or not desc or not est or not fnp :
                    print('Campos vazios')
                    return redirect('/produtos/adproduto',{'usuario_logado':request.session.get('usuario')})
                    
                else:
                    p = Produto(nome=nprod,categoria=catp,preco=preco,img=foto,descricao=desc,estoque=est,fornecedor=fnp,usuario=usuario)

                
                    p.save()
                    print('Fornecedor salva')
                    return redirect(
                        '/produtos/listaprodutos',
                        {
                            'usuario_logado':request.session.get('usuario'),

                        }
                    
                    )
            except Exception as erro:
                print(erro)
                return HttpResponse('Erro ao salvar produto')
        
def listaProdutos(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id=request.session['usuario'])
        prods = Produto.objects.filter(usuario=usuario)
        #return HttpResponse('lISTA FORNECEDORES')
        return render(
            request,
            'produtos.html',
            {
                'usuario_logado':request.session.get('usuario'),
                'prods':prods
            }
        
        )

def verProduto(request,id):
    if request.session.get('usuario'):
        pr = Produto.objects.get(id=id)
        # Evita a falha de segurança de alguém poder mexer no sistema pelo inspecionar
        if request.session.get('usuario') == pr.usuario.id: 
            return render(
                request,
                'verproduto.html',
                {
                    'usuario_logado':request.session.get('usuario'),
                    'pr':pr
                }
            )

def pageditarProduto(request,id):
        if request.session.get('usuario'):
            pr = Produto.objects.get(id=id)
            # Evita a falha de segurança de alguém poder mexer no sistema pelo inspecionar
            if request.session.get('usuario') == pr.usuario.id: 
                return render(
                request,
                'editarproduto.html',
                {
                    'usuario_logado':request.session.get('usuario'),
                    'pr':pr
                }
            )

def edtProdutoBD(request):
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
                    '/produtos/listaprodutos',
                    {
                        'usuario_logado':request.session.get('usuario'),
                        'fn':fn
                    }
                
                )
            except Exception as erro:
                print(erro)
                return HttpResponse('Erro ao editar produto')

def excluirProduto(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id=request.session['usuario'])
        prods = Produto.objects.filter(usuario=usuario)
        produto_id = request.POST.get('produto_id')
        pr = Produto.objects.get(id=produto_id)
        imagem_url = request.POST.get('imagem_prod')
        # Evita a falha de segurança de alguém poder mexer no sistema pelo inspecionar
        if pr.usuario.id == request.session['usuario']:
            try:
                pr = pr.delete()
                remove(f"./{imagem_url}")
                return redirect(
                    '/produtos/listaprodutos',
                    {
                        'usuario_logado':request.session.get('usuario'),
                        'fncd':prods
                    }
                
                )
            except Exception as erro:
                print(erro)
                return HttpResponse('Erro ao excluir produto')
