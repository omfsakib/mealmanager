from django.conf.urls import url
from django.urls import path
from groups.views import groups
from. import views

app_name = 'groups'

urlpatterns = [
    path('',groups.as_view(),name='groups'),
    url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', views.change_friends, name='change_friends'),
]
