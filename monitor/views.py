import json

from django.views.generic import TemplateView
from django.http import HttpResponse

from monitor.models import MemoryLog, SwapLog, CpuLog

def convert_to_mb(byte_size):
    return round(byte_size / 1024 / 1024, 1)

class SummaryView(TemplateView):

    template_name = 'monitor/summary.html'

def memory_data(request):
    if request.is_ajax():
        memory_data = {}
        current_memory_log = MemoryLog.objects.all()[0]
        memory_data.update({
            'used_memory_percent': current_memory_log.percent,
            'used_memory': convert_to_mb(
                current_memory_log.total - current_memory_log.available
            ),
            'total_memory': convert_to_mb(current_memory_log.total),
            'tasks_num': current_memory_log.tasks_num,
            'uptime': str(current_memory_log.uptime),
        })

        return HttpResponse(json.dumps(memory_data), content_type='application/json')

def swap_data(request):
    if request.is_ajax():
        swap_data = {}
        current_swap_log = SwapLog.objects.all()[0]
        swap_data.update({
            'used_swap_percent': current_swap_log.percent,
            'used_swap': convert_to_mb(current_swap_log.used),
            'total_swap': convert_to_mb(current_swap_log.total),
        })

        return HttpResponse(json.dumps(swap_data), content_type='application/json')

def cpu_data(request):
    if request.is_ajax():
        cpu_data = {}
        current_cpu_log = CpuLog.objects.all()[0]
        cpu_data.update({
            'cpu_percent': current_cpu_log.get_percents(),
        })

        return HttpResponse(json.dumps(cpu_data), content_type='application/json')
