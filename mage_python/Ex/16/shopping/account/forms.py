# encoding: utf-8
# Author: Cai Chenyi

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class RegisterFrom(forms.Form):

    username = forms.CharField(widget=forms.TextInput, error_messages={'required': '用户名不能为空'})
    password = forms.CharField(widget=forms.PasswordInput, error_messages={'required': '密码不能为空'})
    password2 = forms.CharField(widget=forms.PasswordInput, required=False)
    email = forms.EmailField(error_messages={'required': '邮箱不能为空', 'invalid': '邮箱格式不正确'})

    def clean_user(self):
        username = self.cleaned_date.get('username', '')
        if len(username) < 6 or len(username) > 16:
            raise forms.ValidationError('用户名长度必须为6到16位')
        try:
            User.objects.get(username=username)
            raise forms.ValidationError("名字已经存在")
        except ObjectDoesNotExist as e:
            pass

        return username


    def clean_password(self):
        password = self.cleaned_date.get('password', '')
        if len(password) < 6 or len(password) > 32:
            raise forms.ValidationError('密码长度必须为6到32位')

        return password


    def clean_password2(self):
        password = self.cleaned_date.get('password', '')
        password2 = self.cleaned_date.get('password2', '')
        if password != password2:
            raise forms.ValidationError('两次密码不一致')

        return password2


    def clean_email(self):
        email = self.cleaned_date.get('email', '')
        try:
            User.objects.get(email=email)
            raise forms.ValidationError('邮箱已经被注册')
        except ObjectDoesNotExist as e:
            pass

        return email
