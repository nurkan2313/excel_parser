# coding:utf-8
from django.shortcuts import render, redirect
from openpyxl import load_workbook
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from models import Goods
from cart.models import Cart, CartItem
from parser_test import excel_reader
from forms import UploadFileForm
from django.contrib import messages


def home(request):
    product = Goods.objects.all().order_by('-id')
    paginator = Paginator(product, 25)
    page = request.GET.get('page')
    try:
        paginator_html = paginator.page(page)
    except PageNotAnInteger:
        paginator_html = paginator.page(1)
    except EmptyPage:
        paginator_html = paginator.page(paginator.num_pages)
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            excel_reader(request.FILES['file'])
            messages.success(request, 'Файл был добавлен')
    else:
        form = UploadFileForm()
    return render(request, 'base/base.html', {'form': form, 'paginator_html': paginator_html})

