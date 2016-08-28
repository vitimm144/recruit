from django.db import models


class Empresa(models.Model):
    nome = models.CharField(
        max_length=255,
        verbose_name='Nome Fantazia'
    )
    razao_social = models.CharField(
        max_length=255,
        verbose_name='Razão Social'
    )
    cnpj = models.CharField(
        max_length=255,
        verbose_name='CNPJ'
    )
    telefone = models.CharField(
        max_length=50,
        verbose_name='Telefone',
        null=True
    )
    website = models.CharField(
        max_length=255,
        verbose_name='Website',
        null=True
    )
    linkedin = models.CharField(
        max_length=255,
        verbose_name='LinkedIN',
        null=True
    )

    def __str__(self):
        return self.nome
