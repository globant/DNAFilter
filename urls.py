import socket

from django.conf.urls.defaults import *
import settings.common as c

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'dnafilter.views.index'),
    url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': c.STATIC_PATH}),
    url(r'^filter$', 'dnafilter.views.filter'),
    (r'^admin/', include(admin.site.urls)),
)

 
