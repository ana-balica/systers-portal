from django.forms import ModelForm
from workspace.models import Resource


class ResourceForm(ModelForm):
    class Meta:
        model = Resource
        exclude = ['date', 'author']
