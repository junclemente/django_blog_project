# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-08 20:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20181108_0529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 8, 20, 56, 9, 440947, tzinfo=utc)),
        ),
    ]
