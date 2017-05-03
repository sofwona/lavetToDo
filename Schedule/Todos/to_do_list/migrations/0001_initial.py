# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-02 10:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('text', models.TextField(max_length=300)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime(2017, 5, 2, 10, 33, 57, 62131))),
            ],
        ),
    ]
