from django.db import models


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
