from django.shortcuts import render

# Create your views here.
from . import models


def index(request):
    print(models.get_messages())
    context = {'messages': models.get_messages()}
    return render(request, 'online/index.html', context)

def create():
    return render(request, 'online/')