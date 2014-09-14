__author__ = 'charles'

from django.conf.urls import patterns, url
from blogger import views

urlpatterns = patterns('',
                       url(r'^$', views.Index.as_view(), name='Index'),
                       url(r'^post/$', views.PostView.as_view(), name='Post'),
                        )