# encoding: utf-8
# Author: Cai Chenyi
from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),
]