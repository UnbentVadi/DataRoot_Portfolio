from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$', 'myprof.views.index'),
    url(r'^profile/', 'myprof.views.profile'),
    url(r'^login', 'myprof.views.login'),
    url(r'^logout', 'myprof.views.logout'),
]
