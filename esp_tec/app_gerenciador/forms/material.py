"""
Form do Projeto
"""
from django import forms
from app_gerenciador.models import Material

# pylint: disable=too-few-public-methods
class MaterialForm(forms.ModelForm):
    """
    Declara o form do Projeto
    """

    class Meta:
        """
        Define os campos que compõem o form
        """
        model = Material

        fields = [
            'nome',
            'unidade_medida'
        ]

        widgets = {
            'nome': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'unidade_medida' : forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }

        labels = {
            'nome': 'Nome',
            'unidade_medida': 'Unidade de Medida'
        }
