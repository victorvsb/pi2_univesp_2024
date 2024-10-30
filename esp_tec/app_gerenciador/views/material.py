"""
View do Material
"""
from typing import Any
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)

from django.db.models import Q

from django.core.paginator import Paginator
from django.urls import reverse_lazy

from app_gerenciador.models import Material
from app_gerenciador.forms.material import MaterialForm

@method_decorator(login_required(login_url='/auth/login/'), name='dispatch')
class MaterialListView(ListView):
    """
    Classe que herda o ListView para implementar a listagem
    de Projetos
    """
    model =Material
    template_name = 'material/list.html'
    paginate_by = 10
    paginator_class = Paginator

    def get_queryset(self):
        """
        Sobrescreve o método get_queryset()
        """

        result = super().get_queryset().order_by('nome')

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
class MaterialCreateView(CreateView):
    """
    Classe que herda o CreateView para implementar
    a criação de Projetos
    """
    model = Material
    form_class = MaterialForm
    template_name = "material/form.html"
    success_url = reverse_lazy('material_list')
    actions = ['material_adicionar']

