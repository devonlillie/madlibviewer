# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-13 22:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(max_length=32)),
                ('description', models.CharField(max_length=32, null=True)),
                ('fill_in', models.CharField(max_length=32, null=True)),
                ('part_of_speech', models.CharField(choices=[('Noun', 'NN'), ('Plural Noun', 'NNS'), ('Adjective', 'JJ'), ('Adverb', 'RB'), ('Verb', 'VB'), ('Verb ending with ing', 'VBG')], max_length=16, null=True)),
            ],
        ),
    ]
