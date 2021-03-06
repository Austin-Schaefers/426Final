# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 01:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ISBN', models.IntegerField(max_length=13)),
                ('title', models.CharField(max_length=25)),
                ('edition', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=12)),
                ('lastName', models.CharField(max_length=12)),
                ('password', models.CharField(max_length=12)),
                ('email', models.EmailField(default='', max_length=254)),
                ('school', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='sid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Student'),
        ),
    ]
