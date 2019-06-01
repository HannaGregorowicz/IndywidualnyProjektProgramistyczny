from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^', include('about.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^about/', include('about.urls')),
    url(r'^contact/', include('contact.urls')),
    url(r'^members/', include('members.urls')),
    url(r'^projects/', include('projects.urls')),
    url(r'^register/', include('users.urls')),
    url(r'^login/', login, {"template_name": "users/login.html"}, name='login'),
    url(r'^logout/', logout, {"template_name": "users/logout.html"}, name='logout'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)