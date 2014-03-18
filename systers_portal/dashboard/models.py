from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class Community(models.Model):
    title = models.CharField(name="Title", max_length=255, blank=False, null=False)
    country = CountryField(null=False)


class User(models.Model):
    auth_user = models.OneToOneField(User, blank=True, null=True)
    organization = models.ManyToManyField(Community, null=True)
