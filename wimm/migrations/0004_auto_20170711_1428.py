# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-11 11:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wimm', '0003_auto_20170711_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daystate',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
