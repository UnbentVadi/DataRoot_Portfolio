from django.conf.urls import include, url
from . import views
from djauth.views import index, profile, login, logout

urlpatterns = [
    url(r'^$', index),
    url(r'^profile/', profile),
    url(r'^login', login),
    url(r'^logout', logout),
]

