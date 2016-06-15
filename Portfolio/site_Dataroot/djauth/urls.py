from django.conf.urls import url
from djauth.views import index, myprofile, login, logout

urlpatterns = [
    url(r'^$', index),
    url(r'^myprofile/', myprofile),
    url(r'^login', login),
    url(r'^logout', logout),
]

