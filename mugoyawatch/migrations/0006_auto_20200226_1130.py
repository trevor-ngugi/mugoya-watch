# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-02-26 08:30
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('mugoyawatch', '0005_posts_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='message',
            field=tinymce.models.HTMLField(),
        ),
    ]
