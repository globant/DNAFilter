import socket

from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()


production_imgs = '/var/www/dnafilterD/dnafilter/static'
local_imgs = '/home/sebastian/Projects/dnafilter/dnafilter_d2/dnafilter/static'

urlpatterns = patterns('',
    url(r'^$', 'dnafilter.views.index'),
    url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': local_imgs if socket.gethostname() == 'glb7765' else production_imgs}),
    url(r'^filter$', 'dnafilter.views.filter'),
    (r'^admin/', include(admin.site.urls)),
)

 
