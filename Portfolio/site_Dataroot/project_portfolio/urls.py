from django.conf.urls import patterns, url
from django.contrib import admin
from . import views

urlpatterns = patterns('',
    url(r'^(?P<accauntuser_id>[0-9]+)/$', 'project_portfolio.views.profile1'),
    url(r'^(?P<accauntuser_id>[0-9]+)/(?P<projectname_id>[0-9]+)/$', 'project_portfolio.views.project_detail')
)

