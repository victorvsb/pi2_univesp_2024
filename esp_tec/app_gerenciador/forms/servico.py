"""
Form do Servico
"""
from django import forms
from app_gerenciador.models import Servico

# pylint: disable=too-few-public-methods
class ServicoForm(forms.ModelForm):
    """
    Declara o form do Servico
    """

    class Meta:
        """
        Define os campos que compõem o form
        """
        model = Servico

        fields = [
            'codigo',
            'nome',
            'descricao',
            'unidade_medida',
            'quantidade'
        ]

        widgets = {
            'codigo': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'nome': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'descricao': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 3,
                    'cols': 20
                }
            ),
            'unidade_medida': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'quantidade': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }

        labels = {
            'codigo': 'Código',
            'nome': 'Nome',
            'descricao': 'Descrição',
            'unidade_medida': 'Unidade de Medida',
            'quantidade': 'Quantidade'
        }
