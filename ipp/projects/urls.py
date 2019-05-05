from django.conf.urls import url
from . import views

app_name = 'projects'

urlpatterns = [
    # /projects/
    url(r'^$', views.index, name='index'),

    # /projects/id
    url(r'^(?P<project_id>[0-9]+)/$', views.detail, name='detail'),
]
