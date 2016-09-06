from django.db import models


class Vaga(models.Model):
    STATUS = (
        ('EA', 'Em aberto'),
        ('AN', 'Em análise'),
        ('AC', 'Aceito'),
        ('RE', 'Recusado'),
    )

    titulo = models.CharField(
        max_length=255,
        verbose_name='Título da vaga'
    )
    resumo = models.TextField(
        verbose_name='Resumo da vaga'
    )
    localidade = models.TextField(
        verbose_name='Resumo da vaga'
    )
    salario = models.CharField(
        max_length=255,
        verbose_name='Salário'
    )
    beneficios = models.CharField(
        max_length=255,
        verbose_name='Benefícios',
        null=True
    )
    descricao = models.TextField(
        verbose_name='Descrição completa',
        null=True
    )
    area_atuacao = models.ForeignKey(
        'core.AreaAtuacao',
        verbose_name='Área de Atuação'
    )
    valor = models.CharField(
        max_length=255,
        verbose_name='Valor',
        null=True
    )
    status = models.CharField(
        max_length=2,
        choices=STATUS,
        verbose_name='Status',
        default='EA'
    )

    def __str__(self):
        return self.titulo
