#!/bin/python

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path = sys.path + [BASE_DIR]
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PiMonitor.settings')

from PIL import Image, ImageDraw
from datetime import timedelta
from django.conf import settings
from django.utils import timezone

from monitor.models import MemoryLog

def render_memory_graph():
    img = Image.open(os.path.join(settings.BASE_DIR, 'scripts', 'base_graph.png'))
    draw = ImageDraw.Draw(img)
    end = timezone.now()
    start = end - timedelta(hours=end.hour, minutes=end.minute, seconds=end.second)
    logs = MemoryLog.objects.filter(datetime__range=[start, end])
    prev_hour = 0
    prev_log = None
    for log in logs:
        if log.datetime.hour != prev_hour:
            prev_hour = log.datetime.hour
            if prev_log:
                start_x = prev_log.datetime.hour * 25 + 20
                start_y = 400 - prev_log.percent / 10 * 35
                end_x = log.datetime.hour * 25 + 20
                end_y = 400 - log.percent / 10 * 35
                draw.line(
                    ((start_x, start_y), (end_x, end_y)), fill='#21dd30', width=5
                )
            prev_log = log

    img.save(os.path.join(
        settings.BASE_DIR, 'media', 'memory_graph_{}.png'.format(
            timezone.now().strftime('%d%m%y%H')
        )
    ), 'PNG')

if __name__ == '__main__':
    render_memory_graph()
