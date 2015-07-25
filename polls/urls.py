from django.conf.urls import include, url
from polls.views import QuestionsList, QuestionDetail, AnswerList
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # Examples:
    # url(r'^$', 'vox_pop_api.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'question/all/$', QuestionsList.as_view()),

    url(r'question/detail/(?P<pk>[0-9]+)/$', QuestionDetail.as_view()),
    url(r'question/detail/(?P<pk>[0-9]+)/answer/all/$', AnswerList.as_view()),

    # url(r'search/(?P<search_str>[a-zA-Z0-9_.-]*)$/', 'users_search', name='users_search'),
    ]
