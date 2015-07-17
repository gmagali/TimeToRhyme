from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('TimeToRhyme.views',
    # Examples:
    # url(r'^$', 'TimeToRhyme.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', 'home', name='home'),
    url(r'^aboutUs/', 'aboutUs', name='aboutUs'),
)
