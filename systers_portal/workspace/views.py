from urllib import urlencode

from django.shortcuts import render, redirect
from django.http.request import QueryDict

from workspace.forms import ResourceForm
from workspace.models import Resource


def index(request):
    return render(request, 'index.html')


def add_resource(request):
    form = ResourceForm()
    if request.method == 'POST':
        resource_params = request.POST.dict()
        resource_params[u"author"] = unicode(request.user.id)
        resource = ResourceForm(resource_params)
        resource.save()
        return redirect(index)
    return render(request, 'add_resource.html', {'form': form})