from django.contrib import admin
from .models import accauntUser, projectName, linkAddress

# Register your models here.

class ArticleInline(admin.StackedInline):
	model = projectName
	extra = 1

class admin_start(admin.ModelAdmin):
	inlines = [ArticleInline]

class linkAdmin(admin.ModelAdmin):
	pass

admin.site.register(accauntUser, admin_start)
admin.site.register(linkAddress, linkAdmin)
