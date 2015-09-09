from django.db import models

class MemoryLog(models.Model):

    total = models.BigIntegerField()
    available = models.BigIntegerField()
    percent = models.PositiveSmallIntegerField()
    datetime = models.DateTimeField()

    class Meta:
        verbose_name = 'Memory Log'
        verbose_name_plural = 'Memory Logs'
        ordering = ['datetime']

class SwapLog(models.Model):

    total = models.BigIntegerField()
    used = models.BigIntegerField()
    free = models.BigIntegerField()
    percent = models.PositiveSmallIntegerField()
    datetime = models.DateTimeField()

    class Meta:
        verbose_name = 'Swap Log'
        verbose_name_plural = 'Swap Logs'
        ordering = ['datetime']
