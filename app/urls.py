from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_produtos, name='lista_produtos'),
    path('novo/', views.criar_produto, name='criar_produto'),
    path('editar/<int:pk>/', views.editar_produto, name='editar_produto'),
    path('deletar/<int:pk>/', views.deletar_produto, name='deletar_produto'),
    path('consultar-cep/', views.consultar_cep, name='consultar_cep'),
]