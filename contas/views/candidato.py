from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from contas.forms import CandidatoForm
from contas.models import Candidato
from django.core.urlresolvers import reverse


class CandidatoCreate(CreateView):
    model = Candidato
    form_class = CandidatoForm
    template_name = 'candidato_form.html'

    def get_success_url(self):
        return reverse('candidato_list')


class CandidatoUpdate(UpdateView):
    model = Candidato
    form_class = CandidatoForm
    template_name = 'candidato_form.html'

    def get_success_url(self):
        return reverse('candidato_list')


class CandidatoDelete(DeleteView):
    model = Candidato
    # template_name_suffix = 'templates/'
    template_name = 'candidato_confirm_delete.html'

    def get_success_url(self):
        return reverse('candidato_list')


class CandidatoListView(ListView):
    model = Candidato
    template_name = 'candidato_list.html'
