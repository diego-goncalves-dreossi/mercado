from django.urls import path
from . import views

app_name = 'sistema'
urlpatterns = [
    path('inicio/',views.inicio, name='inicio'),
    path('sobre/',views.sobre, name="sobre"),
    path('pagjson/',views.pagJSON,name='pagjson'),
    path('pagjson/gerarjson',views.gerarJSON,name="gerarjson"),
    path('pagjson/pagexportar',views.pagJSONExp,name='pagexportar'),
    path('pagjson/pagexportar/categorias/',views.exportarCategorias,name='exportarcategorias'),
    path('pagjson/pagexportar/fornecedores/',views.exportarFornecedores,name='exportarfornecedores'),
    path('pagjson/pagexportar/produtos/',views.exportarProdutos,name='exportarprodutos'),
    path('pagjson/pagexportar/pedidos/',views.exportarPedidos,name='exportarpedidos'),
   

]