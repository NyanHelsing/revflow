# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-13 23:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20170112_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='action',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='view',
            field=models.TextField(blank=True, null=True),
        ),
    ]