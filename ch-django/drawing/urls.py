from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^users/(?P<user_id>[0-9]+)/works/$', views.userworks, name='userworks'),
    url(r'^ranking/(?P<kind>[a-z].*)/$', views.ranking, name='ranking'),
    url(r'^log/$', views.log, name='log'),
]