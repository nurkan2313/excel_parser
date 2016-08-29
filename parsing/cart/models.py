from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.utils import timezone

from linkparser.models import Goods


class CartItem(models.Model):
    product = models.ForeignKey(Goods)
    quantity = models.IntegerField(default=1)
    timestamp = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        try:
            return str(self.cart.id)
        except:
            return self.product.title


class Cart(models.Model):
    user = models.OneToOneField(User)
    cart = models.ManyToManyField(CartItem, related_name='cart')
