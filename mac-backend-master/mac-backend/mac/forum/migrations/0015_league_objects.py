# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-28 12:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0014_handicap_to_match'),
    ]

    operations = [
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo', models.ImageField(blank=True, height_field='logo_height', null=True, upload_to='leagues/logos', width_field='logo_width')),
                ('logo_width', models.PositiveIntegerField(blank=True, editable=False, null=True)),
                ('logo_height', models.PositiveIntegerField(blank=True, editable=False, null=True)),
            ],
        ),
    ]