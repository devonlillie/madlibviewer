# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-13 23:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('madlibs', '0002_auto_20160813_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='field',
            name='parent_title',
            field=models.CharField(default='An Ass', max_length=32),
            preserve_default=False,
        ),
    ]
