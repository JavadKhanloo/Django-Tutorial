from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('به فروشگاه آنلاین ما خوش آمدید')


def all_products(request):
    return HttpResponse('صفحه محصولات')
