
from django.conf.urls import patterns, url
from quiz import views as quiz_view


urlpatterns = patterns('quiz.view',
    url(r'^$', quiz_view.index, name='index'),
    url(r'^submit/$', quiz_view.submit , name='submit'),
    url(r'^question/(?P<type_id>\d+)/$', quiz_view.cat_questions , name='cat_questions'),
    #url(r'^question/$', quiz_view.cat_questions , name='cat_questions'),
    url(r'^question_level/(?P<level_id>\d+)/$', quiz_view.level_questions, name="level_questions"),
    url(r'^login/$',quiz_view.login, name="login"),
    url(r'^exam/(?P<id>\d+)/$', quiz_view.exam, name="exam"),
)
