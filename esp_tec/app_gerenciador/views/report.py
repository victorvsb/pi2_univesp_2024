"""
Gerador de PDF
"""
from datetime import date
from io import BytesIO
from xhtml2pdf import pisa

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from django.template.loader import get_template
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render

from app_gerenciador.models import Projeto



@method_decorator(login_required(login_url='/auth/login/'), name='dispatch')
class ProjectReport(DetailView):
    """
    Classe que herda o DetailView para implementar
    o Relatório do Projeto
    """
    model = Projeto
    # pylint: disable=no-member
    queryset = Projeto.objects.all()
    template_name = "report.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["hoje"] = date.today()
        return context

def render_to_pdf(template_src, context_dict):
    """ Render de pdf baseado em um template html """

    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode('ISO-8859-1')), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


class ViewPDF(View):
    """ Rota para o PDF """
    # pylint: disable=unused-argument
    # pylint: disable=no-self-use
    def get(self, request, *args, **kwargs):
        """ Método get """
        id_projeto = kwargs['pk']
        # pylint: disable=no-member
        projeto = Projeto.objects.get(id=id_projeto)
        context = {
            'object': projeto,
            'hoje': date.today()
        }
        pdf = render_to_pdf('report.html',context)
        return HttpResponse(pdf, content_type='application/pdf')


def home(request):
    """ Rota para a página inicial """
    return render(request, 'home.html')
