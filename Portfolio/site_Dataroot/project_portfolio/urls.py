from django.conf.urls import patterns, url, include
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^1', 'project_portfolio.views.profile1'),
)
