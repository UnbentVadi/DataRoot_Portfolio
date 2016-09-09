from django.conf.urls import url
from django.contrib import admin
from .views import MyUserDetailView, LinkDeatailView, iframe_page, EditView, EditPictureView, delete_project, LinksPaginationView

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', MyUserDetailView.as_view(template_name = 'project_portfolio/profile.html'), name='Profile'),
    url(r'^(?P<pk>[0-9]+)/project/(?P<projectname_id>[0-9]+)/$', LinkDeatailView.as_view(template_name = 'project_portfolio/project.html'), name = 'Project'),
    url(r'^(?P<pk>[0-9]+)/updates/$', LinksPaginationView.as_view(template_name='project_portfolio/updates.html'), name='Updates'),
    url(r'^(?P<id>[0-9]+)/iframe/(?P<pk>[0-9]+)/$', iframe_page, name = "iframe"),
    url(r'^(?P<pk>[0-9]+)/project/(?P<projectname_id>[0-9]+)/delete/$', delete_project, name = 'delete'),
    url(r'^(?P<pk>[0-9]+)/settings/$', EditView.as_view(template_name='project_portfolio/settings.html'), name = "edit"),
    url(r'^(?P<pk>[0-9]+)/settings/picture/$', EditPictureView.as_view(template_name='project_portfolio/settings.html'), name = "EditPicture"),
    url(r'^(?P<pk>[0-9]+)/updated/$', EditView.as_view(template_name='project_portfolio/settings.html'), name = "updated"),
    url(r'^(?P<pk>[0-9]+)/updates/finish_pages/$', MyUserDetailView.as_view(template_name = 'project_portfolio/active.html') , name = "finish_pages"),
    url(r'^(?P<pk>[0-9]+)/updates/progress_pages/$', MyUserDetailView.as_view(template_name = 'project_portfolio/progress_pages.html') , name = "progress_pages"),
    url(r'^(?P<pk>[0-9]+)/updates/new_pages/$', MyUserDetailView.as_view(template_name = 'project_portfolio/new_pages.html') , name = "new_pages"),
]

