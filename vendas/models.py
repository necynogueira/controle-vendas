from django.db import models


class Produto(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    nome = models.CharField(max_length=100)
    quantidade_estoque = models.IntegerField()
    preco_unidade = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome
