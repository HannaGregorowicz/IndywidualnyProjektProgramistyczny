from django.conf.urls import url
from . import views

app_name = 'projects'

urlpatterns = [
    # /projects/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /projects/id
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    #/projects/add/
    url(r'add/$', views.ProjectCreate.as_view(), name='project-add'),
]
