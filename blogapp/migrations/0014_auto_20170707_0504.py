# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-07 05:04
from __future__ import unicode_literals

from django.db import migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0013_article_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=django_markdown.models.MarkdownField(blank=True),
        ),
    ]
