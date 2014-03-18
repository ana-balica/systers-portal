from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class Community(models.Model):
    title = models.CharField(name="Title", max_length=255, blank=False, null=False)
    country = CountryField(null=False)

    def __unicode__(self):
        return self.title


class User(models.Model):
    auth_user = models.OneToOneField(User, blank=True, null=True)
    organization = models.ManyToManyField(Community, null=True)

    def __unicode__(self):
        firstname = self.auth_user.first_name
        lastname = self.auth_user.last_name
        if firstname and lastname:
            return "{0} {1}".format(self.auth_user.first_name, self.auth_user.last_name)
        else:
            return self.auth_user.username
