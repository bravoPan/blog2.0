# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-28 09:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0033_comment_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='avatar',
            field=models.CharField(blank=True, default='matt', max_length=40, null=True),
        ),
    ]
