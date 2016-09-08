from contas.forms import ContratanteForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from contas.models import Contratante
from django.core.urlresolvers import reverse


class ContratanteCreate(CreateView):
    model = Contratante
    form_class = ContratanteForm
    template_name = 'contratante_form.html'

    def get_success_url(self):
        return reverse('contratante_list')


class ContratanteUpdate(UpdateView):
    model = Contratante
    form_class = ContratanteForm
    template_name = 'contratante_form.html'

    def get_success_url(self):
        return reverse('contratante_list')


class ContratanteDelete(DeleteView):
    model = Contratante
    # template_name_suffix = 'templates/'
    template_name = 'contratante_confirm_delete.html'

    def get_success_url(self):
        return reverse('contratante_list')


class ContratanteListView(ListView):
    model = Contratante
    template_name = 'contratante_list.html'
