# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-06 15:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20171106_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cal4_ans',
            name='estate',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='cal4_ans',
            name='spendEnd',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='cal4_ans',
            name='spendEnd2',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='cal4_ans',
            name='successName',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='cal4_ans',
            name='successName2',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
