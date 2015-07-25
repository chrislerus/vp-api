from django.conf.urls import include, url
import users.urls
import polls.urls


urlpatterns = [
    # Examples:
    # url(r'^$', 'vox_pop_api.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^users/', include(users.urls)),
    url(r'^polls/', include(polls.urls)),
    ]
