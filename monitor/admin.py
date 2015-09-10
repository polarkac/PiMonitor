from django.contrib import admin
from monitor.models import *

admin.site.register(CpuLog)
admin.site.register(MemoryLog)
admin.site.register(SwapLog)
admin.site.register(NetLog)