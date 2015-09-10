import json
import psutil
import math

from datetime import datetime
from django.views.generic import TemplateView
from django.http import HttpResponse

def convert_to_mb(byte_size):
    return round(byte_size / 1024 / 1024, 1)

class SummaryView(TemplateView):

    template_name = 'monitor/summary.html'

def memory_data(request):
    memory = psutil.virtual_memory()
    boot_time = psutil.boot_time()
    uptime = datetime.now() - datetime.fromtimestamp(boot_time)
    hours = uptime.seconds / 3600
    minutes = (hours - math.floor(hours)) * 60
    seconds = (minutes - math.floor(minutes)) * 60
    memory_data = {
        'used_memory_percent': memory.percent,
        'used_memory': convert_to_mb(memory.total - memory.available),
        'total_memory': convert_to_mb(memory.total),
        'tasks_num': len(psutil.pids()),
        'uptime': '{days} days {hours:02.0f}:{minutes:02.0f}:{seconds:02.0f}'.format(
            days=uptime.days, hours=hours,
            minutes=minutes, seconds=seconds
        ),
    }

    return HttpResponse(json.dumps(memory_data), content_type='application/json')

def swap_data(request):
    swap = psutil.swap_memory()
    swap_data = {
        'used_swap_percent': swap.percent,
        'used_swap': convert_to_mb(swap.used),
        'total_swap': convert_to_mb(swap.total),
    }

    return HttpResponse(json.dumps(swap_data), content_type='application/json')

def cpu_data(request):
    cpu = psutil.cpu_percent(percpu=True)
    cpu_data = {
        'cpu_percent': cpu,
    }

    return HttpResponse(json.dumps(cpu_data), content_type='application/json')

def net_data(request):
    net = psutil.net_io_counters()
    net_data = {
        'bytes_recv': net.bytes_recv,
        'bytes_sent': net.bytes_sent,
    }

    return HttpResponse(json.dumps(net_data), content_type='application/json')
