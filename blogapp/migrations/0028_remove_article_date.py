# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-28 01:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0027_remove_comment_auto_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='date',
        ),
    ]
