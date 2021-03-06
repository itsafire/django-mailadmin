# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-04 21:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mailadmin', '0009_externalreceiver'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mailinglist',
            name='redirects',
        ),
        migrations.AlterField(
            model_name='externalreceiver',
            name='mailing_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='external_receiver', to='mailadmin.Mailinglist'),
        ),
        migrations.AlterField(
            model_name='externalreceiver',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
