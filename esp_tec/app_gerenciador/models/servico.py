"""Definição do modelo de Serviço"""

from django.db import models

class Servico(models.Model):
    """
    Modelo da persistência de Serviços
    """

    codigo = models.CharField(
        max_length=100,
        verbose_name='Codigo do serviço',
        null=True
    )

    nome = models.CharField(
        max_length=100,
        verbose_name='Nome do serviço'
    )

    descricao = models.TextField(
        verbose_name='Descrição'
    )

    unidade_medida = models.CharField(
        max_length=15,
        verbose_name='Unidade de medida',
        null=True
    )

    quantidade = models.CharField(
        max_length=15,
        verbose_name='Quantidade',
        null=True
    )

    def __str__(self):
        """Sobrescreve o __str__() """
        return str(self.codigo)

    class Meta:
        """Plural do nome da classe"""
        verbose_name_plural = "Serviços"
