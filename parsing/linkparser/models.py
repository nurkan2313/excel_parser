# coding:utf-8
from __future__ import unicode_literals

from django.db import models


class Goods(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)

    class Meta:
        verbose_name = u'Товар'
        verbose_name_plural = u'Товары'

    def __unicode__(self):
        return self.title or u''
