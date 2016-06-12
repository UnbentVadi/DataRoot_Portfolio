from django.conf.urls import url, patterns, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns('',
    url(r'^admin/', admin.site.urls),
    url(r'^', include('project_portfolio.urls'))
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
       'document_root': settings.MEDIA_ROOT}))
    