"""Definição do modelo de Material"""

from django.db import models

class Material(models.Model):
    """
    Modelo da persistência de Materiais
    """

    nome = models.CharField(
        max_length=100,
        verbose_name='Nome do material'
    )

    unidade_medida = models.CharField(
        max_length=15,
        verbose_name='Unidade de medida'
    )

    class Meta:
        """Plural do nome da classe"""
        verbose_name_plural = "Materiais"

    def __str__(self):
        """Sobrescreve o __str__() """
        return str(self.nome)
