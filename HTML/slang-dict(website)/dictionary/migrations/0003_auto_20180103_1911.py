# Generated by Django 2.0.1 on 2018-01-03 19:11

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dictionary', '0002_auto_20180103_1910'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bas',
            new_name='Baslik',
        ),
    ]
