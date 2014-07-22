from django.conf.urls import patterns, include, url
from HelloWorldApp.views import foo, home
#from blog.views import HelloTemplate
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', foo, name='home123'),
    url(r'^blogs/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'HelloWorldApp/$', foo),
    #url(r'^hello/', 'blog.views.hello'),
    #url(r'^hello_template/$', 'blog.views.hello_template'),
    #url(r'^hello_template_simple/$', 'blog.views.hello_template_simple'),
    #url(r'^hello_class_view/$', HelloTemplate.as_view()),
    url(r'^myapp/', include('myapp.urls')),
    # user authentication urls
    url(r'^accounts/login/$', 'djangoapp.views.login'),
    url(r'^accounts/auth/$', 'djangoapp.views.auth_view'),
    url(r'^accounts/login/accounts/auth/$', 'djangoapp.views.auth_view'),
    url(r'^accounts/logout/$', 'djangoapp.views.logout'),
    url(r'^accounts/loggedin/$', 'djangoapp.views.loggedin'),
    url(r'^accounts/invalid/$', 'djangoapp.views.invalid_login'),
    url(r'^accounts/register/$', 'djangoapp.views.register_user'),
    url(r'^accounts/register_success/$', 'djangoapp.views.register_success'),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += patterns('',
    url(r'^places/(?P<name>\w+)/$', home, name='places.view_place')
)
