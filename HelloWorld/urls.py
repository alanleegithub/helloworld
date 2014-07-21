from django.conf.urls import patterns, include, url
from HelloWorldApp.views import foo, home
from blog.views import HelloTemplate
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', foo, name='home123'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'HelloWorldApp/$', foo),
    url(r'^hello/', 'blog.views.hello'),
    url(r'^hello_template/$', 'blog.views.hello_template'),
    url(r'^hello_template_simple/$', 'blog.views.hello_template_simple'),
    url(r'^hello_class_view/$', HelloTemplate.as_view()),
    url(r'^myapp/', include('myapp.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += patterns('',
    url(r'^places/(?P<name>\w+)/$', home, name='places.view_place')
)
