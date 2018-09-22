# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-22 14:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='related_list',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='lists.List'),
        ),
    ]
