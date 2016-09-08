from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from core.forms import VagaForm
from core.models import Vaga
from django.core.urlresolvers import reverse


class VagaCreate(CreateView):
    model = Vaga
    form_class = VagaForm
    template_name = 'vaga_form.html'

    def get_success_url(self):
        return reverse('vaga_list')


class VagaUpdate(UpdateView):
    model = Vaga
    form_class = VagaForm
    template_name = 'vaga_form.html'

    def get_success_url(self):
        return reverse('vaga_list')


class VagaDelete(DeleteView):
    model = Vaga
    # template_name_suffix = 'templates/'
    template_name = 'vaga_confirm_delete.html'

    def get_success_url(self):
        return reverse('vaga_list')


class VagaListView(ListView):
    model = Vaga
    template_name = 'vaga_list.html'
