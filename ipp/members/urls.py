from django.conf.urls import url
from . import views

app_name = 'members'

urlpatterns = [
    # /members
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /members/id
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /members/add
    url(r'add/$', views.MemberCreate.as_view(), name='member-add'),

    # /members/3/update
    url(r'^(?P<pk>[0-9]+)/update/$', views.MemberUpdate.as_view(), name='member-update'),

    # /members/3/delete
    url(r'^(?P<pk>[0-9]+)/delete/$', views.MemberDelete.as_view(), name='member-delete'),
]
