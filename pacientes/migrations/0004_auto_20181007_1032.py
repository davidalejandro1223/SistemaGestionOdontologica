# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-10-07 15:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0003_auto_20181007_0842'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='arl',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='cargo_aspirado',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='eps',
        ),
    ]
