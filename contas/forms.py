from django.forms import ModelForm
from contas.models import Contratante
from contas.models import Recrutador
from contas.models import Candidato


class ContratanteForm(ModelForm):
    class Meta:
        model = Contratante
        fields = '__all__'


class RecrutadorForm(ModelForm):
    class Meta:
        model = Recrutador
        fields = '__all__'


class CandidatoForm(ModelForm):
    class Meta:
        model = Candidato
        fields = '__all__'
