# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-13 16:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('technologies', models.CharField(max_length=500)),
                ('photo', models.FileField(upload_to='')),
                ('more', models.TextField()),
            ],
        ),
    ]
