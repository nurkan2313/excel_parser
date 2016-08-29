from django.contrib import admin
from .models import Cart, CartItem

# Register your models here.


class CartAdmin(admin.ModelAdmin):
    filter_horizontal = ('cart', )


admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem)