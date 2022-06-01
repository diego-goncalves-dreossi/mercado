from django.urls import path
from . import views

app_name = 'sistema'
urlpatterns = [
    path('inicio/',views.inicio, name='inicio'),
    path('sobre/',views.sobre, name="sobre"),
    path('novoproduto/',views.adProduto,name="novoproduto",),
    path('setores/',views.listaSetores, name="setores"),
    path('produtos/',views.listaProdutos,name="produtos"),
    path('filiais/',views.listaFiliais,name="filiais"),
    path('fornecedores/',views.listaFornecedores,name="fornecedores"),
]