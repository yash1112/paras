# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-07 19:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0002_auto_20170305_0348'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.ImageField(upload_to='img')),
                ('answer', models.CharField(max_length=256)),
            ],
        ),
    ]
