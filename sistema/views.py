from django.http import HttpResponse
from django.shortcuts import render

def inicio(request):
    return render(request,'inicio.html',{'usuario_logado':request.session.get('usuario')})

def sobre(request):
    return render(request,'sobre.html',{'usuario_logado':request.session.get('usuario')})