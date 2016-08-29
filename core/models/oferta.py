from django.db import models


class Oferta(models.Model):

    STATUS = (
        ('AN', 'Em análise'),
        ('AC', 'Aceito'),
        ('RE', 'Recusado'),
    )

    valor = models.CharField(
        max_length=255,
        verbose_name='Valor'
    )
    status = models.CharField(
        max_length=2,
        choices=STATUS,
        verbose_name='Status'
    )
    vaga = models.ForeignKey(
        'core.Vaga',
        verbose_name='Vaga'
    )

    def __str__(self):
        return self.valor
