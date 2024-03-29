# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-06 00:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaAtuacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('codigo', models.CharField(max_length=10, null=True, verbose_name='Código')),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome Fantazia')),
                ('razao_social', models.CharField(max_length=255, verbose_name='Razão Social')),
                ('cnpj', models.CharField(max_length=255, verbose_name='CNPJ')),
                ('telefone', models.CharField(max_length=50, null=True, verbose_name='Telefone')),
                ('website', models.CharField(max_length=255, null=True, verbose_name='Website')),
                ('linkedin', models.CharField(max_length=255, null=True, verbose_name='LinkedIN')),
            ],
        ),
        migrations.CreateModel(
            name='Vaga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255, verbose_name='Título da vaga')),
                ('resumo', models.TextField(verbose_name='Resumo da vaga')),
                ('localidade', models.TextField(verbose_name='Resumo da vaga')),
                ('salario', models.CharField(max_length=255, verbose_name='Salário')),
                ('beneficios', models.CharField(max_length=255, null=True, verbose_name='Benefícios')),
                ('descricao', models.TextField(null=True, verbose_name='Descrição completa')),
                ('valor', models.CharField(max_length=255, null=True, verbose_name='Valor')),
                ('status', models.CharField(choices=[('EA', 'Em aberto'), ('AN', 'Em análise'), ('AC', 'Aceito'), ('RE', 'Recusado')], default='EA', max_length=2, verbose_name='Status')),
                ('area_atuacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.AreaAtuacao', verbose_name='Área de Atuação')),
            ],
        ),
    ]
