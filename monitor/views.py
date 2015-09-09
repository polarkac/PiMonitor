import json

from django.views.generic import TemplateView
from django.http import HttpResponse

from monitor.models import MemoryLog, SwapLog

class SummaryView(TemplateView):

    template_name = 'monitor/summary.html'

def memory_data(request):
    if request.is_ajax():
        memory_data = {}
        current_memory_log = MemoryLog.objects.all()[0]
        memory_data.update({
            'used_memory': current_memory_log.percent,
        })

        return HttpResponse(json.dumps(memory_data), content_type='application/json')

def swap_data(request):
    if request.is_ajax():
        swap_data = {}
        current_swap_log = SwapLog.objects.all()[0]
        swap_data.update({
            'used_swap': current_swap_log.percent
        })

        return HttpResponse(json.dumps(swap_data), content_type='application/json')
