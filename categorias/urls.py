from django.urls import path
from . import views

app_name = 'categorias'
urlpatterns = [
    path('listacategorias/',views.listaCategoria, name="listacategorias"),
    path('listacategorias/categoria<int:id>',views.verCategoria,name="vercategoria"),
    path('listacategorias/editarcategoria<int:id>',views.pageditarCategoria,name="editarcategoria"),
    path('editarcategoria',views.edtCategoriaBD,name="editarcategoriabd"),
    path('adcategoria/',views.adCategoria,name="adcategoria"),
    path('adcategoriaBD/',views.adCategoriasBD,name="categoriasbd"),

]