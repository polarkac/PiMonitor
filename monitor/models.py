from django.db import models
from django.utils import timezone

class MemoryLog(models.Model):

    total = models.BigIntegerField()
    available = models.BigIntegerField()
    percent = models.PositiveSmallIntegerField()
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
