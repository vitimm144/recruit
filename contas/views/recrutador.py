from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from contas.forms import RecrutadorForm
from contas.models import Recrutador
from django.core.urlresolvers import reverse


class RecrutadorCreate(CreateView):
    model = Recrutador
    form_class = RecrutadorForm
    template_name = 'recrutador_form.html'

    def get_success_url(self):
        return reverse('recrutador_list')


class RecrutadorUpdate(UpdateView):
    model = Recrutador
    form_class = RecrutadorForm
    template_name = 'recrutador_form.html'

    def get_success_url(self):
        return reverse('Recrutador_list')


class RecrutadorDelete(DeleteView):
    model = Recrutador
    # template_name_suffix = 'templates/'
    template_name = 'recrutador_confirm_delete.html'

    def get_success_url(self):
        return reverse('recrutador_list')


class RecrutadorListView(ListView):
    model = Recrutador
    template_name = 'recrutador_list.html'
