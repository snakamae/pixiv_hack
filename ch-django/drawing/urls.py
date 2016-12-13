from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^log/$', views.log, name='log'),
    url(r'^image_view/$', views.image_view, name='image_view')
]