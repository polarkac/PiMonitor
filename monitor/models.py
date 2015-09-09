import json

from django.db import models
from django.utils import timezone

class MemoryLog(models.Model):

    total = models.BigIntegerField()
    available = models.BigIntegerField()
    percent = models.PositiveSmallIntegerField()
    tasks_num = models.IntegerField()
    uptime = models.DurationField()
    datetime = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Memory Log'
        verbose_name_plural = 'Memory Logs'
        ordering = ['-datetime']

    def __str__(self):
        return 'Memory used: {}%'.format(self.percent)

class SwapLog(models.Model):

    total = models.BigIntegerField()
    used = models.BigIntegerField()
    free = models.BigIntegerField()
    percent = models.PositiveSmallIntegerField()
    datetime = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Swap Log'
        verbose_name_plural = 'Swap Logs'
        ordering = ['-datetime']

    def __str__(self):
        return 'Swap used: {}%'.format(self.percent)

class CpuLog(models.Model):

    percents = models.CharField(max_length=50)
    datetime = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'CPU log'
        verbose_name_plural = 'CPU logs'
        ordering = ['-datetime']

    def get_percents(self):
        return json.loads(self.percents)

    def __str__(self):
        return 'CPU used: {}'.format(self.percents)
