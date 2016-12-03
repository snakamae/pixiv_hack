from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^users/(?P<user_id>[0-9]+)/works/$', views.userworks, name='userworks'),
    url(r'^ranking/(?P<kind>[a-z].*)/high/$', views.ranking_high, name='ranking_high'),
    url(r'^ranking/(?P<kind>[a-z].*)/mid/$', views.ranking_mid, name='ranking_mid'),
    url(r'^ranking/(?P<kind>[a-z].*)/low/$', views.ranking_low, name='ranking_low'),
    url(r'^log/$', views.log, name='log'),
]