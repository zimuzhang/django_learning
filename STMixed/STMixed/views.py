# -*- coding:utf-8 -*-
from django.shortcuts import render

def home(request):
    print '============'
    return render(request, 'home.html', locals())