from django.db import models
from django.core.urlresolvers import reverse


class AreaAtuacao(models.Model):
    nome = models.CharField(
        max_length=255,
        verbose_name='Nome'
    )
    codigo = models.CharField(
        max_length=10,
        verbose_name='Código',
        null=True
    )

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('area_atuacao_edit', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('area_atuacao_delete', kwargs={'pk': self.pk})