"""Definição do modelo de Projeto"""

from django.db import models

from . import Material, Servico

# pylint: disable=too-few-public-methods
class Projeto(models.Model):
    """
    Modelo da persistência de Projetos
    """
    
    nome = models.CharField(
        max_length=100,
        verbose_name='Nome do projeto'
    )

    descricao = models.TextField(
        verbose_name='Descrição'
    )

    dt_criacao = models.DateField(
        verbose_name='Data de criação'
    )

    lista_de_materiais = models.ManyToManyField(
        Material,
        verbose_name='Lista de materiais'
    )

    lista_de_servicos = models.ManyToManyField(
        Servico,
        verbose_name='Lista de codigo de serviços',
    )

    def __str__(self):
        """Sobrescreve o __str__() """
        return str(self.nome)

    class Meta:
        """Plural do nome da classe"""
        verbose_name_plural = "Projetos"
