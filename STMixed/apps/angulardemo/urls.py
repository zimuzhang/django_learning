# -*- coding:utf8 -*-

from django.core.urls import patterns, url

pattern = patterns('apps.angulardemo.views',
    url(r'^$', 'index', name='index'),
)