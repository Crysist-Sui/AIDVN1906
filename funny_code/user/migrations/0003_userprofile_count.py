# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-01-18 11:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200110_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='count',
            field=models.IntegerField(default=0, null=True, verbose_name='统计值'),
        ),
    ]
