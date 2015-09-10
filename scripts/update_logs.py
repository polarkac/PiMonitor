#!/bin/python

import os
import sys
import time
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path = sys.path + [BASE_DIR]
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PiMonitor.settings')

import psutil
from datetime import datetime

from monitor.models import MemoryLog, SwapLog, CpuLog, NetLog

time_sleep = 5
last_bytes_sent = 0
last_bytes_recv = 0

def update_logs():
    global last_bytes_recv, last_bytes_sent

    memory = psutil.virtual_memory()
    swap = psutil.swap_memory()
    cpu = psutil.cpu_percent(percpu=True)
    boot_time = psutil.boot_time()
    uptime = datetime.now() - datetime.fromtimestamp(boot_time)
    tasks_num = len(psutil.pids())
    net = psutil.net_io_counters()
    
    MemoryLog.objects.create(
        total=memory.total, available=memory.available,
        percent=memory.percent, uptime=uptime, tasks_num=tasks_num
    )

    SwapLog.objects.create(
        total=swap.total, used=swap.used, free=swap.free, percent=swap.percent
    )

    CpuLog.objects.create(percents=json.dumps(cpu))

    NetLog.objects.create(
        bytes_sent=net.bytes_sent, bytes_recv=net.bytes_recv,
        kbps_sent=((net.bytes_sent - last_bytes_sent) / time_sleep / 1024),
        kbps_recv=((net.bytes_recv - last_bytes_recv) / time_sleep / 1024)
    )

    last_bytes_sent = net.bytes_sent
    last_bytes_recv = net.bytes_recv

if __name__ == '__main__':
    while(True):
        update_logs()
        time.sleep(5)
