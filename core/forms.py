from django.forms import ModelForm
from core.models import Empresa
from core.models import Vaga


class EmpresaForm(ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'


class VagaForm(ModelForm):
    class Meta:
        model = Vaga
        fields = '__all__'
