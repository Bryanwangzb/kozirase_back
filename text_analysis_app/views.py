from django.shortcuts import render

# Create your views here.

from __future__ import unicode_literals
from django.shortcuts import render


def index(request):
    return render(request, 'text_analysis_app/index.html')
