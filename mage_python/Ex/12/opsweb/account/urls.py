# encoding: utf-8
# Author: Cai Chenyi
from django.conf.urls import url, include
from django.contrib import admin
from . import views, user

urlpatterns = [
    url(r'^hello/$', views.hello),
    url(r'^login/$', user.userlogin),
    url(r'^logout/$', user.userlogout),
    url(r'^user/$', views.UserView.as_view()),
    url(r'^userlist/$', views.UserListView.as_view()),
    url(r'^userlistview/$', views.UserListAsView.as_view()),
]
