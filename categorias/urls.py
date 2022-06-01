from django.urls import path
from . import views

app_name = 'categorias'
urlpatterns = [
    path('categorias/',views.listaCategoria, name="categorias"),
    path('adcat/',views.adCategoria,name="adcategoria"),
    path('adcatBD/',views.adCategoriasBD,name="categoriasbd"),
]