# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-29 23:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_areaatuacao'),
        ('contas', '0004_auto_20160828_1807'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidato',
            name='area_atuacao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.AreaAtuacao', verbose_name='Área de Atuação'),
        ),
        migrations.AddField(
            model_name='recrutador',
            name='area_atuacao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.AreaAtuacao', verbose_name='Área de Atuação'),
        ),
    ]