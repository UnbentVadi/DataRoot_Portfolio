from django.contrib import admin
from .models import MyUser, Projects, Link
from django.contrib.auth.models import User, Group

# Register your models here.

class ArticleInline(admin.StackedInline):
	model = Projects
	extra = 1

class admin_start(admin.ModelAdmin):
	inlines = [ArticleInline]

class linkAdmin(admin.ModelAdmin):
	pass

admin.site.register(MyUser, admin_start)
admin.site.register(Link, linkAdmin)
admin.site.unregister(Group)

