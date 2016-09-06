from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class Usuario(AbstractBaseUser):
    nome = models.CharField(max_length=150, verbose_name='Nome')
    email = models.EmailField(unique=True, verbose_name='Email')
    celular = models.CharField(max_length=30, verbose_name='Celular')
    linkedin = models.CharField(max_length=255, verbose_name='LinkedIN')
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.nome


class Contratante(Usuario):
    skype = models.CharField(max_length=255, verbose_name='Skype')
    email_profissional = models.EmailField(null=True, verbose_name='Email Profissional')
    telefone_empresarial = models.CharField(
        max_length=255,
        null=True,
        verbose_name='Telefone Empresarial'
    )
    empresa = models.ForeignKey('core.Empresa')
    cargo = models.CharField(max_length=255)


class Recrutador(Usuario):
    TIPOS_DE_RECRUTADORES = (
        ('MA', 'Recrutador Master'),
        ('RE', 'Recrutador'),
    )
    tipo_recrutador = models.CharField(choices=TIPOS_DE_RECRUTADORES, default='RE', max_length=2)
    skype = models.CharField(max_length=255, verbose_name='Skype')
    telefone = models.CharField(max_length=255, verbose_name='Telefone', null=True)
    area_atuacao = models.ForeignKey(
        'core.AreaAtuacao',
        verbose_name='Área de Atuação',
        null=True
    )


class Candidato(Usuario):
    curriculo = models.FileField(verbose_name='Currículo')
    analise_recrutador = models.TextField(verbose_name='Análise Recrutador')
    area_atuacao = models.ForeignKey(
        'core.AreaAtuacao',
        verbose_name='Área de Atuação',
        null=True
    )
