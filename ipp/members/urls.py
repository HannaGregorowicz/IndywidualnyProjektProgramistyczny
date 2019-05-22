from django.conf.urls import url
from . import views

app_name = 'members'

urlpatterns = [
    # /members
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /members/id
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'add/$', views.MemberCreate.as_view(), name='member-add'),
]
