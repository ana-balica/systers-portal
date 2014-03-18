from django.shortcuts import render

from models import Resourse


def index(request):
    return render(request, 'index.html')