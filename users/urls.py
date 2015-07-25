from django.conf.urls import include, url
from users.views import Citizens_detail, Citizens_list, Mayor_detail, Mayor_list
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # Examples:
    # url(r'^$', 'vox_pop_api.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'citizen/all/$', Citizens_list.as_view()),
    url(r'mayor/all/$', Mayor_list.as_view()),

    url(r'citizen/detail/(?P<pk>[0-9]+)/$', Citizens_detail.as_view()),
    url(r'mayor/detail/(?P<pk>[0-9]+)/$', Mayor_detail.as_view()),

    # url(r'search/(?P<search_str>[a-zA-Z0-9_.-]*)$/', 'users_search', name='users_search'),
    ]
