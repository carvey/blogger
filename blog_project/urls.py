from django.conf.urls import patterns, include, url
from blogger.views import PostView, CategoryView
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', include('blogger.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^(?P<category>\w+)/$', CategoryView.as_view()),
                       url(r'^(?P<requested_category>[-\w]+)/(?P<slug>[-\w]+)/$', PostView.as_view()),
                       url(r'^weblog/', include('zinnia.urls', namespace='zinnia')),
                       url(r'^comments/', include('django.contrib.comments.urls')),
                       url(r'^photologue/', include('photologue.urls', namespace='photologue')),
                       url(r'^tinymce/', include('tinymce.urls')),

)
