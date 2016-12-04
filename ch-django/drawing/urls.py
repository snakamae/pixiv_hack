from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^ranking/(?P<kind>[a-z].*)/high/$', views.ranking_high, name='ranking_high'),
    url(r'^ranking/(?P<kind>[a-z].*)/mid/$', views.ranking_mid, name='ranking_mid'),
    url(r'^ranking/(?P<kind>[a-z].*)/low/$', views.ranking_low, name='ranking_low'),
    url(r'^demo/$', views.demo_view, name='demo_view'),
    url(r'^log/$', views.log, name='log'),
]