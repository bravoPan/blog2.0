# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-28 01:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0023_auto_20170728_0134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='date',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='auto_date',
        ),
    ]