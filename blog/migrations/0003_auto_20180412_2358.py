# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-12 23:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180412_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 4, 12, 23, 58, 30, 256973)),
        ),
    ]
