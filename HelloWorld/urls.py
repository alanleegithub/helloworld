from django.conf.urls import patterns, include, url
from HelloWorldApp.views import foo, home

#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', foo, name='home123'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'HelloWorldApp/$', foo),
)

urlpatterns += patterns('',
    url(r'^places/(?P<name>\w+)/$', home, name='places.view_place')
)
