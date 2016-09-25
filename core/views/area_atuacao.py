from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from core.forms import AreaAtuacaoForm
from core.models import AreaAtuacao
from django.core.urlresolvers import reverse


class AreaAtuacaoCreate(CreateView):
    model = AreaAtuacao
    form_class = AreaAtuacaoForm
    template_name = 'area_atuacao_form.html'

    def get_success_url(self):
        return reverse('area_atuacao_list')


class AreaAtuacaoUpdate(UpdateView):
    model = AreaAtuacao
    form_class = AreaAtuacaoForm
    template_name = 'area_atuacao_form.html'

    def get_success_url(self):
        return reverse('area_atuacao_list')


class AreaAtuacaoDelete(DeleteView):
    model = AreaAtuacao
    # template_name_suffix = 'templates/'
    template_name = 'area_atuacao_confirm_delete.html'

    def get_success_url(self):
        return reverse('area_atuacao_list')


class AreaAtuacaoListView(ListView):
    model = AreaAtuacao
    template_name = 'area_atuacao_list.html'
