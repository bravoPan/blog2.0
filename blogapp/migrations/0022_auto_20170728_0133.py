# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-28 01:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0021_auto_20170728_0132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateField(blank=True, default=False),
        ),
    ]
