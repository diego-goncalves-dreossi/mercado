import hashlib
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Usuario
# Criar hash pra senha
from hashlib import sha256


# Adaptar todas as views para o projeto de prova de Topicos especiais de informática
# Apenas nomes estão corretos

def login(request):
    if request.session.get('usuario'):
        return redirect('/livro/inicio/')
    status = request.GET.get('status')
    return render(request,'login.html',{'status': status})

def cadastro(request):
    if request.session.get('usuario'):
        return redirect('/livro/inicio/')
    status = request.GET.get('status')
    return render(request,'cadastro.html', {'status': status})


def valida_cadastro(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    csenha = request.POST.get('confirma_senha')

    usuario = Usuario.objects.filter(email = email)
    # Procura no banco de dados se há um usuário com esse email cadastrado

    if len(nome.strip()) == 0 or len(email.strip()) == 0 or senha != csenha:
        return redirect('/cadastro/?status=1')

    if len(senha) < 8:
        return redirect('/cadastro/?status=2')

    if len(usuario) > 0:
        return redirect('/cadastro/?status=3')

    try:
        # Criptografa a senha
        senha = sha256(senha.encode()).hexdigest()
        usuario = Usuario(nome = nome,senha = senha,email = email)
        usuario.save()

        return redirect('/cadastro/?status=0')
    except:
        return redirect('/cadastro/?status=4')

def valida_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    # Mexendo com session
    # Criptografa a senha
    senha = sha256(senha.encode()).hexdigest()
    usuario = Usuario.objects.filter(email = email).filter(senha = senha)

    if len(usuario) == 0:
        return redirect('/login/?status=1')
    elif len(usuario) > 0:
        request.session['usuario'] = usuario[0].id
        return redirect(f'/inicio/?id_usuario={request.session["usuario"]}')
        return HttpResponse('Inicio')

    
    return HttpResponse(f"{email} {senha}")

def sair(request):
    request.session.flush() # Limpa a session
    return redirect('/login/')
