# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-09-14 06:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('bid', models.AutoField(primary_key=True, serialize=False)),
                ('img_url', models.CharField(max_length=100)),
                ('detail_url', models.CharField(max_length=100)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('is_delete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'banner',
                'ordering': ['-bid'],
            },
        ),
    ]
