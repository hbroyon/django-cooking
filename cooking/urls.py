# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from cooking.views import IndexView


urlpatterns = patterns('',
                       url(r'^$', IndexView.as_view(), name='index'))
