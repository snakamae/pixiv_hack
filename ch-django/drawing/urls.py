from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^users/(?P<user_id>[0-9]+)/works/$', views.userworks, name='userworks'),
    url(r'^ranking/$', views.ranking, name='ranking'),
]