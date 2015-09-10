from django.conf.urls import url

from monitor.views import SummaryView, memory_data, swap_data, cpu_data, net_data

urlpatterns = [
    url(r'^$', SummaryView.as_view(), name='monitor-summary'),
    url(r'^memory/$', memory_data, name='monitor-memory_data'),
    url(r'^swap/$', swap_data, name='monitor-swap_data'),
    url(r'^cpu/$', cpu_data, name='monitor-cpu_data'),
    url(r'^net/$', net_data, name='monitor-net_data')
]
