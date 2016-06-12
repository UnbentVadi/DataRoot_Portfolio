from django.contrib import admin
from .models import MyUser, Projects, Link

# Register your models here.

class Article(admin.StackedInline):
	model = Projects
	extra = 1

class Admin_start(admin.ModelAdmin):
	inlines = [Article]

class LinkAdmin(admin.ModelAdmin):
	pass

admin.site.register(MyUser, Admin_start)
admin.site.register(Link, LinkAdmin)
