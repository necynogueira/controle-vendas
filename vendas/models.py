from django.db import models


class Produto(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    nome = models.CharField(max_length=100)
    quantidade_estoque = models.IntegerField()
    preco_unidade = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome


class Venda(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade_vendida = models.PositiveIntegerField()
    data_venda = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.produto.nome} - Quantidade {self.quantidade_vendida}"
