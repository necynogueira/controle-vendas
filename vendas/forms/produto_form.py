from django import forms
from vendas.models import Produto


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['codigo', 'nome', 'quantidade_estoque', 'preco_unidade']
