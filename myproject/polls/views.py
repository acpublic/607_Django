from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from datetime import datetime
import os

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def get(request):
    data = {
        'data1': datetime.now(),
        'data2': os.path.abspath(__file__)
    }
    return render(request, 'polls/index.html', data)
