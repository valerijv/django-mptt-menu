# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Category


def index(request):
    return render(request, 'menu/index.html', {
        'categories': Category.objects.all()
    })