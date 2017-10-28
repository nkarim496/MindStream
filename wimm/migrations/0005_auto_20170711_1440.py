# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-11 11:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wimm', '0004_auto_20170711_1428'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wimm',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='wimm',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='wimm',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]