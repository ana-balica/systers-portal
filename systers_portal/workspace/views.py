from django.shortcuts import render

from workspace.forms import ResourceForm
from workspace.models import Resource


def index(request):
    return render(request, 'index.html')


def add_resource(request):
    form = ResourceForm()
    return render(request, 'add_resource.html', {'form': form})