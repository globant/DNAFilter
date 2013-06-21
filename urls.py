import socket

from django.conf.urls.defaults import *
import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'dnafilter.views.index'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': settings.STATIC_PATH}),
    url(r'^filter$', 'dnafilter.views.filter'),
    (r'^admin/', include(admin.site.urls)),
)

 
