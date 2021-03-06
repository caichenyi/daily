#encoding: utf-8

from django.conf.urls import url

from . import views
from .views import RegisterView, ActiveView

app_name = 'account'

urlpatterns = [
   url(r'^$', views.index, name='index'),
   url(r'^register/', RegisterView.as_view(), name='register'),
   url(r'^active/', ActiveView.as_view(), name='active'),
]
