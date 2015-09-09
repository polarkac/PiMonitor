# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MemoryLog',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('total', models.BigIntegerField()),
                ('available', models.BigIntegerField()),
                ('percent', models.PositiveSmallIntegerField()),
                ('datetime', models.DateTimeField()),
            ],
            options={
                'ordering': ['datetime'],
                'verbose_name': 'Memory Log',
                'verbose_name_plural': 'Memory Logs',
            },
        ),
        migrations.CreateModel(
            name='SwapLog',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('total', models.BigIntegerField()),
                ('used', models.BigIntegerField()),
                ('free', models.BigIntegerField()),
                ('percent', models.PositiveSmallIntegerField()),
                ('datetime', models.DateTimeField()),
            ],
            options={
                'ordering': ['datetime'],
                'verbose_name': 'Swap Log',
                'verbose_name_plural': 'Swap Logs',
            },
        ),
    ]
