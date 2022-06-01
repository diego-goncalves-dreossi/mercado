from django.urls import path
from . import views

app_name = 'categorias'
urlpatterns = [
    path('listacategorias/',views.listaCategoria, name="listacategorias"),
    path('listacategorias/categoria<int:id>',views.verCategoria,name="vercategoria"),
    path('adcategoria/',views.adCategoria,name="adcategoria"),
    path('adcategoriaBD/',views.adCategoriasBD,name="categoriasbd"),

]