# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-17 05:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bodypage', '0006_auto_20161117_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('P', 'PUBLIC'), ('E', 'EDITING'), ('D', 'DELETED'), ('C', 'DELETE-COMPELETLY')], max_length=1, verbose_name='文章状态'),
        ),
    ]