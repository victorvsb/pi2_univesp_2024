from django.contrib import admin
from django.urls import path

from app_gerenciador.views import ProjectReport, ViewPDF, home

from app_gerenciador.views.projeto import (
    ProjetoListView, 
    ProjetoCreateView, 
    ProjetoUpdateView,
    ProjetoDeleteView
)

from app_gerenciador.views.material import(
    MaterialListView,
    MaterialCreateView
)

from app_gerenciador.views.servico import(
    ServicoListView,
    ServicoCreateView
)

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path('report/<int:pk>/',
        ProjectReport.as_view(),
        name = 'report'
    ),
    path('report_pdf/<int:pk>/',
        ViewPDF.as_view(),
        name = 'report_pdf'
    ),
    path('projeto/',
        ProjetoListView.as_view(),
        name = 'projeto_list'
    ),
    path('projeto/adicionar',
        ProjetoCreateView.as_view(),
        name = 'projeto_adicionar'
    ),
    path('projeto/editar/<int:pk>/',
        ProjetoUpdateView.as_view(),
        name = 'projeto_editar'
    ),
     path(
        'projeto/delete/<int:pk>/',
        ProjetoDeleteView.as_view(),
        name = 'projeto_delete'
    ),
    path('', home, name='home'),

    path('material/',
        MaterialListView.as_view(),
        name = 'material_list'
    ),
    path('material/adicionar',
        MaterialCreateView.as_view(),
        name = 'material_adicionar'
    ),
    path('servico/adicionar',
        ServicoCreateView.as_view(),
        name = 'servico_adicionar'
    ),
    path('servico/',
        ServicoListView.as_view(),
        name = 'servico_list'
    ),
]
