# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-14 09:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20170614_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='dept',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='major',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]