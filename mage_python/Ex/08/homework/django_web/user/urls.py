# encoding: utf-8
# Author: Cai Chenyi
from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^login/', views.login, name='login'),
    url(r'^list/', views.list, name='list'),
    url(r'^delete/', views.delete, name='delete'),
    url(r'^modify_request/', views.modify_request, name='modify_request'),
    url(r'^modify/', views.modify, name='modify'),
    url(r'^add_request/', views.add_request, name='add_request'),
    url(r'^add/', views.add, name='add'),
    url(r'^logout/', views.logout, name='logout'),
]