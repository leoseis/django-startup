from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    # /music/ ref to index
    url(r'^$', views.index, name='index'),
    #  music = /712/  ref to detail

    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    # making modifications  btw first bracket on line 8 auto updates to all templates

    url(r'^(?P<album_id>[0-9]+)favorite/$', views.favorite, name='favorite'),
]



