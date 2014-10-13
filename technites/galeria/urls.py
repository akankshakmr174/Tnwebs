# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url, include

from galeria import views
from django.views.generic import ListView,DetailView

urlpatterns = patterns('galeria.views',
    url(
        '^(?P<album_slug>[-\w]+)/(?P<pk>[0-9]+)/(?P<slug>[-\w]+)/$',
        views.PictureDetail.as_view(),
        name='galeria-picture'
    ),
    url(
        '^(?P<slug>[-\w]+)/$',
        views.AlbumDetail.as_view(template_name="album_detail.html"),
        name='galeria-album'
    ),
    url('^$', views.AlbumList.as_view(template_name="album_list.html"), name='galeria-album-list'),
)
