# -*- coding:utf8 -*-

from django.core.urls import patterns, url

pattern = patterns('apps.angular_app.views',
    url(r'^$', 'index', name='index'),
)