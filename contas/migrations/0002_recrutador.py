# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-28 17:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recrutador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('tipo', models.CharField(choices=[('SE', 'Recrutador Senior'), ('MA', 'Recrutador Master'), ('RE', 'Recrutador'), ('CA', 'Candidato'), ('CO', 'Contratante')], max_length=2)),
                ('nome', models.CharField(max_length=150, verbose_name='Nome')),
                ('email', models.EmailField(max_length=254)),
                ('celular', models.CharField(max_length=30, verbose_name='Celular')),
                ('skype', models.CharField(max_length=255, verbose_name='Skype')),
                ('linkedin', models.CharField(max_length=255, verbose_name='LinkedIN')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]