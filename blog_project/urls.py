from django.conf.urls import patterns, include, url
from blogger.views import PostView, CategoryView
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', include('blogger.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^(?P<cat>[-\w]+)/$', CategoryView.as_view()),
                       url(r'^(?P<requested_category>[-\w]+)/(?P<slug>[-\w]+)/$', PostView.as_view()),
                       url(r'^weblog/', include('zinnia.urls', namespace='zinnia')),
                       url(r'^comments/', include('django.contrib.comments.urls')),
                       url(r'^photologue/', include('photologue.urls', namespace='photologue')),
                       url(r'^tinymce/', include('tinymce.urls')),

)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))