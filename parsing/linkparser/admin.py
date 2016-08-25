from django.contrib import admin
from models import Goods
# Register your models here.


class ParserAdmin(admin.ModelAdmin):
    model = Goods
    list_display = ('title', 'price')

admin.site.register(Goods, ParserAdmin)
