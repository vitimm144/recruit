from django.forms import ModelForm
from contas.models import Contratante
from contas.models import Recrutador
from contas.models import Candidato


class ContratanteForm(ModelForm):
    class Meta:
        model = Contratante
        fields = [
            'nome',
            'password',
            'email',
            'email_profissional',
            'celular',
            'telefone_empresarial',
            'skype',
            'linkedin',
            'empresa',
            'cargo'
        ]


class RecrutadorForm(ModelForm):
    class Meta:
        model = Recrutador
        fields = [
            'nome',
            'password',
            'email',
            'tipo_recrutador',
            'celular',
            'telefone',
            'skype',
            'linkedin',
            'area_atuacao'
        ]


class CandidatoForm(ModelForm):
    class Meta:
        model = Candidato
        fields = '__all__'
