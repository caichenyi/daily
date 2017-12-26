# encoding: utf-8
# Author: Cai Chenyi
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate #用户验证
from django.contrib.auth import login #用户登录
from django.contrib.auth import logout #用户退出



def userlogin(request):
    if request.method == "GET":
        return render(request, template_name="user/login.html")
    elif request.method == "POST":
        username = request.POST.get("username", "")
        userpass = request.POST.get("userpass", "")
        user = authenticate(username=username, password=userpass)
        if user is not None:
            # 用户名和密码是正确的
            login(request, user) #写cookie，写session
            return HttpResponseRedirect(request.GET.get('next', '/'))
        else:
            # 用户名或密码错误
            return HttpResponse("用户登录失败")


def userlogout(request):
    logout(request)
    return HttpResponse("用户退出成功")


