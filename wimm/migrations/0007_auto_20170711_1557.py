# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-11 12:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wimm', '0006_auto_20170711_1525'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wimm',
            name='date',
        ),
        migrations.RemoveField(
            model_name='wimm',
            name='time',
        ),
        migrations.AddField(
            model_name='wimm',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
