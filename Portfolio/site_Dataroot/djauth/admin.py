from django.contrib import admin
from project_portfolio.models import Projects, Link


class mylinkAdmin(admin.StackedInline):
    model = Link
    extra = 1


class projectAdmin(admin.ModelAdmin):
    inlines = [
        mylinkAdmin,
    ]


admin.site.register(Projects, projectAdmin)
