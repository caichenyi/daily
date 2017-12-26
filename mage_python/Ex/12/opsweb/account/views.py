from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth.decorators import login_required #login装饰器，检查cookie和session
from django.views.generic import View, TemplateView
from django.views.generic import ListView #分页显示
from django.contrib.auth.models import User
from django.core.paginator import Paginator #分页显示

@login_required
def hello(request):
    return HttpResponse("hello")


class UserView(View):

    def get(self, request):
        return render(request, template_name="user/create.html")

    def post(self, request):
        User.objects.create_user(request.POST.get("username", ""),
                                 request.POST.get("email", ""),
                                 request.POST.get("userpass", "")) #添加用户
        return HttpResponse("post")


class UserListView(TemplateView):
    template_name = "user/userlist.html"

    def get_context_data(self, **kwargs):
        # 这个方法就可以将变量传到模板里
        context = super(UserListView, self).get_context_data(**kwargs)
        try:
            page = int(self.request.GET.get("page", "1"))
        except:
            page = 1

        paginator = Paginator(User.objects.all(), 10)
        page = paginator.page(page)

        context["object_list"] = page.object_list
        context["page_obj"] = page
        return context


