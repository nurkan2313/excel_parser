from __future__ import unicode_literals

from django.db import models
from linkparser import Goods
# Create your models here.


class CustomerCart(models.Model):
    items = models.ManyToManyField(Goods, null=True, blank=True)


class CartItems(models.Model):
    pass