from django.http import HttpResponse
from django.shortcuts import redirect, render
from autenticacao.models import Usuario
from fornecedores.models import Fornecedor
from os import remove
from pedidos.models import Pedido
from produtos.models import Produto
"""
request.session.get('usuario'): Se usuário está logado 
request.method == 'POST': Se função foi alcançada atraves de um botão, não atraves de escrevendo na barra de pesquisa
request.session.get('usuario') == cat.usuario.id: Evita a falha de segurança de alguém poder mexer no sistema pelo inspecionar
"""
def adPedido(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id=request.session['usuario'])
        produtos = Produto.objects.filter(usuario=usuario)
        ped = Pedido.objects.all()
        return render(request,'adpedido.html',{'usuario_logado':request.session.get('usuario'),'produtos':produtos,'ped':ped[0]})

def adPedidoBD(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id=request.session['usuario'])
        produtos = Produto.objects.filter(usuario=usuario)
        pedidos = Pedido.objects.filter(usuario=usuario)

        if request.method == 'POST':
            p = request.POST.get('ped_produto')
            produto = Produto.objects.get(id=p)
            filial = request.POST.get('filial')
            qnt = request.POST.get('qnt')
            pagamento = request.POST.get('pag_pedido')
            status = request.POST.get('sts_pedido')

            if not filial or not qnt or not pagamento:
                print('Campos vazios')
                return redirect('/pedidos/adpedido',{'usuario_logado':request.session.get('usuario')})
                
            else:
                pedido = Pedido(produto=produto,filial=filial,pagamento=pagamento,qntnovosprods=qnt,status=status,usuario=usuario)

            try:
                pedido.save()
                print('Pedido salvo')

                if status == 'Entregue' or status == 'En':
                    pa = Produto.objects.get(id=p)
                    pa.estoque = str(int(pa.estoque) + int(qnt))
                    pa.save()

                return redirect(
                    '/pedidos/listapedidos',
                    {
                        'usuario_logado':request.session.get('usuario'),
                        'pedidos':pedidos
                    }
                
                )
            except Exception as erro:
                print(erro)
                return HttpResponse('Erro ao salvar pedido')
        
def listaPedidos(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id=request.session['usuario'])
        pedidos = Pedido.objects.filter(usuario=usuario)
    
        return render(
            request,
            'pedidos.html',
            {
                'usuario_logado':request.session.get('usuario'),
                'pedidos':pedidos
            }
        
        )

def verPedido(request,id):
    if request.session.get('usuario'):
        pedido = Pedido.objects.get(id=id)
        print(pedido.pagamento)
        # Evita a falha de segurança de alguém poder mexer no sistema pelo inspecionar
        if request.session.get('usuario') == pedido.usuario.id: 
            return render(
                request,
                'verpedido.html',
                {
                    'usuario_logado':request.session.get('usuario'),
                    'ped':pedido
                }
            )

def pageditarPedido(request,id):
        if request.session.get('usuario'):
            ped = Pedido.objects.get(id=id)
            print(ped.produto.id)
            # Evita a falha de segurança de alguém poder mexer no sistema pelo inspecionar
            if request.session.get('usuario') == ped.usuario.id: 
                return render(
                request,
                'editarpedido.html',
                {
                    'usuario_logado':request.session.get('usuario'),
                    'ped':ped
                }
            )

def edtPedidoBD(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id=request.session['usuario'])
        pedido_id = request.POST.get('pedido_id')
        p = request.POST.get('ped_produto')
        filial = request.POST.get('filial')
        qnt = request.POST.get('qnt')
        pagamento = request.POST.get('pag_pedido')
        status = request.POST.get('sts_pedido')
        pedidos = Pedido.objects.filter(usuario=usuario)
        pe = Pedido.objects.get(id=pedido_id)
        pedidos = Pedido.objects.filter(usuario=usuario)

        # Evita a falha de segurança de alguém poder mexer no sistema pelo inspecionar
        if pe.usuario.id == request.session['usuario'] and request.method == 'POST':
            try:
                pe.filial = filial
                pe.qntnovosprods = qnt
                pe.pagamento = pagamento
                pe.status = status

                if status == 'Entregue' or status == 'En':
                    pa = Produto.objects.get(id=p)
                    pa.estoque = pa.estoque + qnt
                    pa.save()
                
                pe.save()
                return redirect(
                    '/pedidos/listapedidos',
                    {
                        'usuario_logado':request.session.get('usuario'),
                        'pedidos':pedidos
                    }
                
                )
            except Exception as erro:
                print(erro)
                return HttpResponse('Erro ao editar pedido')

def excluirPedido(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id=request.session['usuario'])
        pedidos = Pedido.objects.filter(usuario=usuario)
        pedido_id = request.POST.get('pedido_id')
        pedido = Pedido.objects.get(id=pedido_id)
        # Evita a falha de segurança de alguém poder mexer no sistema pelo inspecionar
        if pedido.usuario.id == request.session['usuario']:
            try:
                pedido = pedido.delete()
                
                return redirect(
                    '/pedidos/listapedidos',
                    {
                        'usuario_logado':request.session.get('usuario'),
                        'pedidos':pedidos
                    }
                
                )
            except Exception as erro:
                print(erro)
                return HttpResponse('Erro ao excluir fornecedor')

