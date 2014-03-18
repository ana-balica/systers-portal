from django.conf.urls import patterns, include, url
from django.contrib import admin

from workspace.views import index

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', index, name="index"),
    url(r'^index$', index, name="index"),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
