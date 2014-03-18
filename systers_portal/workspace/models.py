from django.db import models
from dashboard.models import User

RESOURCE_TYPES = (
    ('scholarship', 'Scholarship'),
    ('grant', 'Grant'),
    ('internship', 'Internship'),
    ('workshop', 'Workshop'),
    ('development', 'Professional Development'),
    ('meetup', 'Meetup')
)

class Resourse(models.Model):
    type = models.CharField(max_length=255, choices=RESOURCE_TYPES)
    author = models.ForeignKey(User, null=False)
    title = models.CharField(max_length=511, blank=False, null=False)
    content = models.TextField()
