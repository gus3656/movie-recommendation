# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-13 03:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_text', models.CharField(max_length=200)),
                ('release_date', models.DateTimeField(verbose_name='Release Date')),
                ('duration', models.DurationField()),
                ('genre', models.CharField(max_length=200)),
                ('synopsis', models.TextField(max_length=300)),
            ],
        ),
    ]
