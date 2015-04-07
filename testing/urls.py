from django.conf.urls import patterns, include, url
from django.contrib import admin
from tinylibrary.views import webhook_payload, HomeView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testing.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^books/', include('tinylibrary.urls', namespace='tinylibrary')),
    url(r'^payload/', webhook_payload),
)
