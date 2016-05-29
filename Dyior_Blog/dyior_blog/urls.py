#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls import *

urlpatterns = patterns('dyior_blog.views',
                       url(r'article_list$', 'article_list'),
                       url(r'article_view$', 'article_view'),
                       url(r'photo_list$', 'photo_list'),
                       url(r'photo_view', 'photo_view'),
                       url(r'music_list', 'music_list'),
                       url(r'music_view', 'music_view'),
                       url(r'url_list', 'url_list'),
                       url(r'url_view', 'url_view'),
                       )
