from django.urls import path
from . import views

app_name = 'fornecedores'
urlpatterns = [
    path('listafornecedores/',views.listaFornecedores,name="listafornecedores"),
    path('listafornecedores/fornecedor<int:id>',views.verFornecedor,name="verfornecedor"),
    path('listafornecedores/editarfornecedor<int:id>',views.pageditarFornecedor,name="editarfornecedor"),
    path('editarfornecedor/',views.edtFornecedorBD,name="editarfornecedorbd"),
    path('adfornecedor/',views.adFornecedor,name="adfornecedor"),
    path('adfornecedorBD/',views.adFornecedorBD,name="fornecedoresbd"),
    path('excluirfornecedor/',views.excluirFornecedor,name="excluirfornecedor"),
    path('listafornecedores/paginseririmg<int:id>',views.pageNovapaginseririmg,name="paginseririmg"),
    path('alterarimagem/',views.alterarImagem,name="alterarimagem")

]