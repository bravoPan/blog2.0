# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-19 09:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0041_auto_20180618_0734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='avatar_color',
            field=models.CharField(default=False, max_length=20, null=True),
        ),
    ]
