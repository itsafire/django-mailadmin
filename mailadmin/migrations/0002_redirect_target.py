# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-21 16:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailadmin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='redirect',
            name='target',
            field=models.CharField(default='', max_length=300),
        ),
    ]
