from django.urls import path
from . import views

app_name = 'sistema'
urlpatterns = [
    path('inicio/',views.inicio, name='inicio'),
    path('sobre/',views.sobre, name="sobre")
]