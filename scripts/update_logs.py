#!/bin/python

import os
import sys
import time
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path = sys.path + [BASE_DIR]
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PiMonitor.settings')

import psutil

from monitor.models import MemoryLog, SwapLog, CpuLog

def update_logs():
    memory = psutil.virtual_memory()
    swap = psutil.swap_memory()
    cpu = psutil.cpu_percent(percpu=True)

    MemoryLog.objects.create(
        total=memory.total, available=memory.available,
        percent=memory.percent
    )
    SwapLog.objects.create(
        total=swap.total, used=swap.used, free=swap.free, percent=swap.percent
    )
    CpuLog.objects.create(percents=json.dumps(cpu))

if __name__ == '__main__':
    while(True):
        update_logs()
        time.sleep(5)
