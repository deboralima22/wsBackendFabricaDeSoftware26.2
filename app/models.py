from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=120)
    descricao = models.TextField(blank=True)
    sku = models.CharField(max_length=30, unique=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.PositiveIntegerField(default=0)
    estoque_minimo = models.PositiveIntegerField(default=5)
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome