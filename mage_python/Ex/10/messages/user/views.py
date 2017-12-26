from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect

from . import models
from .forms import LoginForm, CreatUser, ViewUser, ViewPassword
from utils import crypt

# Create your views here.

def require_login(request):
    if request.session.get('user'):
        return HttpResponseRedirect('/user/list_user/')
    form = LoginForm()
    return render(request, 'user/login.html', {'form' : form})


def login(request):
    if request.session.get('user'):
        return HttpResponseRedirect('/user/list_user/')
    form = LoginForm(request.POST)
    if form.is_valid():
        request.session['user'] = {'username' : form.cleaned_data['username']}
        return HttpResponseRedirect('/user/list_user/')
    else:
        return render(request, 'user/login.html', {'form' : form})


def list_user(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')
    users = models.User2.objects.all()
    print(users)
    context = {'users': users}
    return render(request, 'user/list.html', context)


def delete_user(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')
    _id = request.GET.get('id', '')
    models.User2.objects.get(pk=_id).delete()
    return HttpResponseRedirect('/user/list_user/')


def create_user(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')
    form = CreatUser(request.POST)
    return render(request, 'user/create.html', {'form': form})


def save_user(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')
    form = CreatUser(request.POST)
    if form.is_valid():
        user = models.User2(username=form.cleaned_data['username'], \
                            password=crypt.CryptUtils.md5(form.cleaned_data['password']), \
                            tel=form.cleaned_data['tel'], age=form.cleaned_data['age'])
        user.save()
        return HttpResponseRedirect('/user/list_user/')
    else:
        return render(request, 'user/create.html', {'form': form})


def view_user(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')
    uid = request.GET.get('id', '')
    form = ViewUser()
    return render(request, 'user/view.html', {'form': form, 'id': uid})
    # uid = request.GET.get('id', '')
    # user = models.User.get_by_id(uid)
    # return render(request, 'user/view.html', {'user' : user})

def modify_user(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')
    uid = request.POST.get('id', '')
    form = ViewUser(request.POST)
    if form.is_valid():
        models.User2.objects.filter(pk=uid).update(username=form.cleaned_data['username'], \
                                                   tel=form.cleaned_data['tel'], \
                                                   age=form.cleaned_data['age'])
        return HttpResponseRedirect('/user/list_user/')
    else:
        return render(request, 'user/view.html', {'form': form, 'id': uid})


def view_password(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')
    uid = request.GET.get('id', '')
    form = ViewPassword()
    return render(request, 'user/view_pwd.html', {'form': form, 'id': uid})


def modify_password(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')
    uid = request.POST.get('id', '')
    form = ViewPassword(request.POST)
    if form.is_valid():
        models.User2.objects.filter(pk=uid).update(password=crypt.CryptUtils.md5(form.cleaned_data['password']))
        return HttpResponseRedirect('/user/list_user/')
    else:
        return render(request, 'user/view_pwd.html', {'form': form, 'id': uid})


def logout(request):
    request.session.flush()
    return HttpResponseRedirect('/user/require_login/')
