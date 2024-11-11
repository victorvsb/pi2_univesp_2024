"""
View do Servico
"""
from typing import Any
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views.generic import (
    ListView,
    CreateView
)

from django.db.models import Q

from django.core.paginator import Paginator
from django.urls import reverse_lazy

from app_gerenciador.models import Servico
from app_gerenciador.forms.servico import ServicoForm

@method_decorator(login_required(login_url='/auth/login/'), name='dispatch')
class ServicoListView(ListView):
    """
    Classe que herda o ListView para implementar a listagem
    de Projetos
    """
    model =Servico
    template_name = 'servico/list.html'
    paginate_by = 10
    paginator_class = Paginator

    def get_queryset(self):
        """
        Sobrescreve o método get_queryset()
        """

        result = super().get_queryset().order_by('codigo')

        search = self.request.GET.get('search', None)
        if search:
            result = result.filter(Q(nome__icontains=search))

        return result

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', None)
        return context


@method_decorator(login_required(login_url='/auth/login/'), name='dispatch')
# pylint: disable=too-many-ancestors
class ServicoCreateView(CreateView):
    """
    Classe que herda o CreateView para implementar
    a criação de Projetos
    """
    model = Servico
    form_class = ServicoForm
    template_name = "servico/form.html"
    success_url = reverse_lazy('servico_list')
    actions = ['servico_adicionar']
