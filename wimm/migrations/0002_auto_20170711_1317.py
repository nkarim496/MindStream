# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-11 10:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wimm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daystate',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
