# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-13 04:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_auto_20170813_1433'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Title',
            new_name='Movie',
        ),
    ]
