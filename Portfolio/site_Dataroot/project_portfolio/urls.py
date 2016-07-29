from django.conf.urls import url
from django.contrib import admin
from .views import MyUserDetailView, LinkDeatailView, iframe_page, EditProfile

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', MyUserDetailView.as_view(template_name = 'project_portfolio/profile.html'), name='Profile'),
    url(r'^(?P<pk>[0-9]+)/project/(?P<projectname_id>[0-9]+)/$', LinkDeatailView.as_view(template_name = 'project_portfolio/project.html'), name = 'Project'),
    url(r'^(?P<pk>[0-9]+)/updates/$', MyUserDetailView.as_view(template_name = 'project_portfolio/updates.html'), name='Updates'),
    url(r'^(?P<pk>[0-9]+)/settings/$', MyUserDetailView.as_view(template_name = 'project_portfolio/settings.html'), name='Settings'),
    url(r'^iframe/(?P<pk>[0-9]+)/$', iframe_page, name = "iframe"),
    url(r'^(?P<pk>[0-9]+)/edit/$', EditProfile, name = "edit"),
    url(r'^(?P<pk>[0-9]+)/updates/finish_pages/$', MyUserDetailView.as_view(template_name = 'project_portfolio/active.html') , name = "finish_pages"),
    url(r'^(?P<pk>[0-9]+)/updates/progress_pages/$', MyUserDetailView.as_view(template_name = 'project_portfolio/progress_pages.html') , name = "progress_pages"),
    url(r'^(?P<pk>[0-9]+)/updates/new_pages/$', MyUserDetailView.as_view(template_name = 'project_portfolio/new_pages.html') , name = "new_pages"),
]

