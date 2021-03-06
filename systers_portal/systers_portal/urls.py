from django.conf.urls import patterns, include, url
from django.contrib import admin

from workspace.views import index, add_resource, view_resources, view_resource
from dashboard.views import login_view, logout_view

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', index, name="home"),
    url(r'^index/', index, name="home"),
    url(r'^resources/$', view_resources, name="view_resources"),
    url(r'^resources/([0-9]+)/', view_resource, name="view_resource"),
    url(r'^resources/add/', add_resource, name="add_resource"),
    url(r'^login/', login_view, name="login"),
    url(r'^logout/', logout_view, name="logout"),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
