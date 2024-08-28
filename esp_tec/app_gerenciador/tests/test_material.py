"""Testes da aplicação app_gerenciador."""
from django.test import TestCase

from models import Material


class MaterialTestCase(TestCase):
    """Teste do modelo Material."""
    def setUp(self):
        # pylint: disable=no-member
        Material.objects.create(
            nome="Areia", unidade_medida="metro cúbico")

    def test_material(self):
        """teste material"""
        # pylint: disable=no-member
        areia = Material.objects.get(nome="Areia")
        self.assertEqual(areia.nome, 'Areia')
