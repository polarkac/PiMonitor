# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0005_auto_20150909_1514'),
    ]

    operations = [
        migrations.CreateModel(
            name='NetLog',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('bytes_sent', models.BigIntegerField()),
                ('bytes_recv', models.BigIntegerField()),
                ('kbps_sent', models.IntegerField()),
                ('kbps_recv', models.IntegerField()),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'Network Logs',
                'verbose_name': 'Network Log',
                'ordering': ['-datetime'],
            },
        ),
    ]
