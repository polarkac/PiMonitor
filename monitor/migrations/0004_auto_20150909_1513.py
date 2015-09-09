# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0003_auto_20150909_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='memorylog',
            name='tasks_num',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='memorylog',
            name='uptime',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 9, 15, 13, 6, 384782, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
