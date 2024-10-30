"""
Módulo de views do app_gerenciador
"""
from .projeto import (
    ProjetoListView,
)

from .material import(
    MaterialListView,
    MaterialCreateView,
)

from .report import (
    ProjectReport,
    render_to_pdf,
    ViewPDF,
    home
)

__all__ = [
    'ProjetoListView',
    'ProjectReport',
    'render_to_pdf',
    'ViewPDF',
    'home',
    'MaterialListView',
    'MaterialCreateView'
]
