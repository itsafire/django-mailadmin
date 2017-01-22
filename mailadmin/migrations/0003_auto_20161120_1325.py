# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-20 12:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailadmin', '0002_redirect_target'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='quota',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='domain',
            name='disabled',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='domain',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
