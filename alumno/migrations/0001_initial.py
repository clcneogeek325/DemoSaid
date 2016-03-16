# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-16 04:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellidos', models.CharField(max_length=200)),
                ('edad', models.IntegerField(max_length=2)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
    ]
