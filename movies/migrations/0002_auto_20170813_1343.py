# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-13 03:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Title',
            new_name='Movies',
        ),
    ]