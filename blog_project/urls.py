from django.conf.urls import patterns, include, url
from blogger.views import PostView, CategoryView
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', include('blogger.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^(?P<category>\w+)/$', CategoryView.as_view()),
                       url(r'^(?P<requested_category>\w+)/(?P<id>[0-9]+)/$', PostView.as_view()),
                       url(r'^weblog/', include('zinnia.urls')),
                       url(r'^comments/', include('django.contrib.comments.urls')),

)
