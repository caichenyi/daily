from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

# Create your views here.
from . import models


def index(request):
    if request.session.get('user') is None:
        return redirect('/user/require_login/')
    print(models.get_messages())
    context = {'messages' : models.get_messages()}
    return render(request, 'online/index.html', context)


def create(request):
    if request.session.get('user') is None:
        return redirect('/user/require_login/')
    return render(request, 'online/create.html')


def save(request):
    if request.session.get('user') is None:
        return redirect('/user/require_login/')
    username = request.GET.get('username', '')
    title = request.GET.get('title', '')
    content = request.GET.get('content', '')
    print(username, title, content)
    models.save_message(username, title, content)
    return HttpResponseRedirect('/online/')
