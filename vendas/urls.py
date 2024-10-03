from django.urls import path
from . import views

urlpatterns = [
    path('produtos/', views.listar_produtos, name='listar_produtos'),
    path('produtos/novo/', views.criar_produto, name='criar_produto'),
    path('produtos/editar/<int:id>/', views.editar_produto, name='editar_produto'),
    path('produtos/excluir/<int:id>/', views.excluir_produto, name='excluir_produto'),
    path('registrar-venda/', views.registrar_venda, name='registrar_venda'),
    path('relatorio-vendas/', views.gerar_relatorio_csv, name='relatorio_vendas'),
    path('relatorio-estoque/', views.gerar_relatorio_estoque, name='relatorio_estoque')
]
