from django.conf.urls import url
from django.contrib import admin
from .views import MyUserDetailView, LinkListView


urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', MyUserDetailView.as_view(), name='MyUser_detail'),
    url(r'^(?P<accauntuser_id>[0-9]+)/project/(?P<projectname_id>[0-9]+)/$', LinkListView.as_view(), name = 'link_list'),
]
