from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from core.forms import EmpresaForm
from core.models import Empresa
from django.core.urlresolvers import reverse


class EmpresaCreate(CreateView):
    model = Empresa
    form_class = EmpresaForm
    template_name = 'empresa_form.html'

    def get_success_url(self):
        return reverse('empresa_list')


class EmpresaUpdate(UpdateView):
    model = Empresa
    form_class = EmpresaForm
    template_name = 'empresa_form.html'

    def get_success_url(self):
        return reverse('empresa_list')


class EmpresaDelete(DeleteView):
    model = Empresa
    # template_name_suffix = 'templates/'
    template_name = 'empresa_confirm_delete.html'

    def get_success_url(self):
        return reverse('empresa_list')


class EmpresaListView(ListView):
    model = Empresa
    template_name = 'empresa_list.html'
