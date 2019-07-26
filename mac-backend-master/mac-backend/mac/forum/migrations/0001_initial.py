# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-16 10:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('string', models.CharField(choices=[('ms1', 'MS1'), ('msx', 'MSX'), ('ms2', 'MS2'), ('cs1-x', 'ÇŞ1-X'), ('cs1-2', 'ÇŞ1-2'), ('csx-2', 'ÇŞX-2'), ('iy1', 'IY1'), ('iyx', 'IYX'), ('iy2', 'IY2'), ('2y1', '2Y1'), ('2yx', '2YX'), ('2y2', '2Y2'), ('au1,5-alt', 'AU1,5-ALT'), ('au1,5-ust', 'AU1,5-UST'), ('au2,5-alt', 'AU2,5-ALT'), ('au2,5-ust', 'AU2,5-UST'), ('au3,5-alt', 'AU3,5-ALT'), ('au3,5-ust', 'AU3,5-UST'), ('iyau1,5-alt', 'IYAU1,5-ALT'), ('iyau1,5-ust', 'IYAU1,5-UST'), ('tg0-1', 'TG0-1'), ('tg2-3', 'TG2-3'), ('tg4-6', 'TG4-6'), ('tg7+', 'TG7+'), ('h1', 'H1'), ('hx', 'HX'), ('h2', 'H2'), ('kgvar', 'KGVAR'), ('kgyok', 'KGYOK'), ('tctek', 'TCTEK'), ('tccift', 'TCCIFT'), ('iyms1/1', 'IYMS1/1'), ('iyms1/x', 'IYMS1/x'), ('iyms1/2', 'IYMS1/2'), ('iymsx/x', 'IYMSx/x'), ('iymsx/1', 'IYMSx/1'), ('iymsx/2', 'IYMSx/2'), ('iyms2/2', 'IYMS2/2'), ('iyms2/x', 'IYMS2/x'), ('iyms2/1', 'IYMS2/1')], max_length=20)),
                ('odd', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_team', models.CharField(max_length=100)),
                ('away_team', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('score', models.CharField(max_length=20)),
                ('iyscore', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=500)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.Match')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, max_length=500, null=True)),
                ('upvote', models.PositiveIntegerField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.Game')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='match',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.Match'),
        ),
        migrations.AlterUniqueTogether(
            name='prediction',
            unique_together=set([('game', 'user')]),
        ),
    ]
