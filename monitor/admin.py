from django.contrib import admin
from .models import *

admin.site.register(CpuLog)
admin.site.register(MemoryLog)
admin.site.register(SwapLog)
admin.site.register(NetLog)