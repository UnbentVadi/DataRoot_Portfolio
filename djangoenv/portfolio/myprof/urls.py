from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$', 'myprof.views.login'),
    url(r'^profile/', 'myprof.views.template_three_simple'),
    url(r'^login', 'myprof.views.login'),
    url(r'^logout', 'myprof.views.logout'),
]
