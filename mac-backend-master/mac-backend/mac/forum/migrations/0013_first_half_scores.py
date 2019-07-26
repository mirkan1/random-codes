# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-15 19:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0012_iddaa_id_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='first_half_score',
        ),
        migrations.AddField(
            model_name='match',
            name='away_first_half_score',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='match',
            name='home_first_half_score',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
