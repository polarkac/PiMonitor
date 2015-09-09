# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0002_auto_20150909_0856'),
    ]

    operations = [
        migrations.CreateModel(
            name='CpuLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('percents', models.CharField(max_length=50)),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['-datetime'],
                'verbose_name_plural': 'CPU logs',
                'verbose_name': 'CPU log',
            },
        ),
        migrations.AlterModelOptions(
            name='memorylog',
            options={'verbose_name_plural': 'Memory Logs', 'ordering': ['-datetime'], 'verbose_name': 'Memory Log'},
        ),
        migrations.AlterModelOptions(
            name='swaplog',
            options={'verbose_name_plural': 'Swap Logs', 'ordering': ['-datetime'], 'verbose_name': 'Swap Log'},
        ),
    ]
