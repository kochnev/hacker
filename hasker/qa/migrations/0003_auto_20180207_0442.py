# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-07 04:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0002_auto_20180206_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(blank=True, to='qa.Tag'),
        ),
    ]
