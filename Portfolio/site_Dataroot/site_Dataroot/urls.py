from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),# admin 
    url(r'^profile/', include('project_portfolio.urls')),# profile or related to it 
    url(r'', include('djauth.urls')), # registration
]

