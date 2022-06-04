from django.urls import path
from . import views

app_name = 'pedidos'
urlpatterns = [
    path('listapedidos/',views.listaPedidos,name="listapedidos"),
    path('listapedidos/pedido<int:id>',views.verPedido,name="verpedido"),
    path('listapedidos/editarpedido<int:id>',views.pageditarPedido,name="editarpedido"),
    path('editarpedido/',views.edtPedidoBD,name="editarpedidobd"),
    path('adpedido/',views.adPedido,name="adpedido"),
    path('adpedidoBD/',views.adPedidoBD,name="pedidobd"),
    path('excluirpedido/',views.excluirPedido,name="excluirpedido"),
]