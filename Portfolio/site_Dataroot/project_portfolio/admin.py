from django.contrib import admin
from .models import MyUser, Projects, Link
from django.contrib.auth.models import User, Group


admin.site.register(MyUser)
admin.site.unregister(Group)

