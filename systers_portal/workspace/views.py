from urllib import urlencode

from django.shortcuts import render, redirect
from django.http.request import QueryDict

from workspace.forms import ResourceForm
from workspace.models import Resource
from dashboard.models import User


def index(request):
    return render(request, 'index.html')


def add_resource(request):
    form = ResourceForm()
    if request.method == 'POST':
        form = ResourceForm(request.POST)
        resource = form.save(commit=False)
        resource.author = User(request.user.id)
        resource.save()
        return redirect(index)
    return render(request, 'add_resource.html', {'form': form})

def view_resources(request):
    resources = Resource.objects.all()
    return render(request, 'resources.html', {'resources': resources})
