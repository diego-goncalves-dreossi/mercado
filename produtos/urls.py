from django.urls import path
from . import views

app_name = 'produtos'
urlpatterns = [
    path('listaprodutos/',views.listaProdutos,name="listaprodutos"),
    path('listaprodutos/produto<int:id>',views.verProduto,name="verproduto"),
    path('listaprodutos/editarproduto<int:id>',views.pageditarProduto,name="editarproduto"),
    path('editarproduto/',views.edtProdutoBD,name="editarprodutobd"),
    path('adproduto/',views.adProduto,name="adproduto"),
    path('adprodutoBD/',views.adProdutoBD,name="produtobd"),
    path('excluirproduto/',views.excluirProduto,name="excluirproduto"),
    path('listaprodutos/paginseririmg<int:id>',views.pageNovapaginseririmg,name="paginseririmg"),
    path('alterarimagem/',views.alterarImagem,name="alterarimagem")

]