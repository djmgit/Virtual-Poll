from django.conf.urls import url

from . import views

app_name='polls'

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.login_form, name='login_form'),
    url(r'^login/', views.login_form, name='login_form'),
    url(r'^login_view/', views.login_view, name='login_view'),

    url(r'^index/', views.index, name='index'),
    url(r'^logout/', views.logout_view, name='logout'),

    url(r'^signup/', views.signup_form, name='signup_form'),
    url(r'^signup_view/', views.signup_view, name='signup_view'),
    url(r'^add_question/', views.add_question, name='add_question'),
    url(r'^save_question/', views.save_question, name='save_question'),


    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

    url(r'^(?P<question_id>[0-9]+)/comment/$', views.comment, name='comment'),
]


'''
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
'''