from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *

# Create your views here.
def index(request):
    menu = ['Home', "About", "Contact", "Settings"]
    posts = News.objects.all()
    
    return render(request, 'news/index.html', {'title':"Home", "menu": menu, "posts":posts})

def about(request):
    menu = ['Home', "About", "Contact", "Settings"]
    return render(request,'news/about.html', {'title':"About","menu": menu})

def category(request):
    return HttpResponse("<h1>News - Category</h1>")