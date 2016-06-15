from django.conf.urls import url, patterns, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^profile/', include('project_portfolio.urls')),
    #url(r'', include('djauth.urls')),
]
