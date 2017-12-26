from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from . import models

# Create your views here.

def index(request):
    return render(request, 'user/index.html')

def login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    rt_status, rt_reason = models.validate_login(username, password)
    if rt_status:
        request.session['user'] = rt_status
        content = {'users': models.get_users()}
        return render(request, 'user/list.html', content)
        # return HttpResponseRedirect('/user/list/')
    else:
        content = {'username': username, 'password': password, 'error': rt_reason}
        return render(request, 'user/index.html', content)

def list(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/index/')
    field = request.POST.get('list', '')
    users = models.get_users()
    return render(request, 'user/list.html', {'users': models.list_user(users, field)})

def delete(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/index/')
    username = request.GET.get('username', '')
    models.delete_user(username)
    return HttpResponseRedirect('/user/list/')

def modify_request(request):
    username = request.GET.get('username', '')
    return render(request, 'user/modify.html', {'username': username})

def modify(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/index/')
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    tel = request.POST.get('tel', '')
    age = request.POST.get('age', '')
    rt_status, rt_reason = models.validate_modify(username, password, tel, age)
    if rt_status:
        models.modify_user(username, password, tel, age)
        return HttpResponseRedirect('/user/list/')
    else:
        content = {'username': username, 'password': password, 'tel': tel, 'age': age, 'error': rt_reason}
        return render(request, 'user/modify.html', content)

def add_request(request):
    return render(request, 'user/add.html')

def add(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/index/')
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    tel = request.POST.get('tel', '')
    age = request.POST.get('age', '')
    rt_status, rt_reason = models.validate_add(username, password, tel, age)
    if rt_status:
        models.add_user(username, password, tel, age)
        return HttpResponseRedirect('/user/list/')
    else:
        content = {'username': username, 'password': password, 'tel': tel, 'age': age, 'error': rt_reason}
        return render(request, 'user/add.html', content)

def logout(request):
    request.session.flush()
    return HttpResponseRedirect('/user/index/')