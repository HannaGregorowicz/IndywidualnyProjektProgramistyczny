from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('about.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^about/', include('about.urls')),
    url(r'^contact/', include('contact.urls')),
    url(r'^members/', include('members.urls')),
    url(r'^projects/', include('projects.urls')),
]
