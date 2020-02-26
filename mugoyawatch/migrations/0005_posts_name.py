# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-02-26 08:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mugoyawatch', '0004_posts'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
