from datetime import date

from django.db import models
from dashboard.models import User
from django_countries.fields import CountryField

RESOURCE_TYPES = (
    ('scholarship', 'Scholarship'),
    ('grant', 'Grant'),
    ('internship', 'Internship'),
    ('workshop', 'Workshop'),
    ('development', 'Professional Development'),
    ('meetup', 'Meetup')
)

RESOURCE_STATUS = {
    ('upcoming', 'Upcoming'),
    ('past', 'Past')
}

class Resource(models.Model):
    type = models.CharField(max_length=255, choices=RESOURCE_TYPES)
    author = models.ForeignKey(User, null=False)
    date = models.DateField(default=date.today)
    title = models.CharField(max_length=511, blank=False, null=False)
    status = models.CharField(max_length=31, choices=RESOURCE_STATUS)
    location = CountryField()
    content = models.TextField()
