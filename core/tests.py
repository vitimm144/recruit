from django.test import TestCase
from core.models import Empresa


class ModelTestCase(TestCase):

    def test_empresa_model(self):
        empresa = Empresa.objects.create(
            nome='ABC',
            razao_social='LTDA',
            cnpj='11122233345',
            telefone='22223344',
            website='www.abc.com.br',
            linkedin='www.linkedin.com/2342343'
        )
        self.assertEqual(empresa.pk, 1)
        self.assertEqual(empresa.razao_social, 'LTDA')
        self.assertEqual(empresa.cnpj, '11122233345')
        self.assertEqual(empresa.telefone, '22223344')
