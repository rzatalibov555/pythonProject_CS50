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

def show_category(request, cat_id):
    return HttpResponse("<h1>News - Category {cat_id}</h1>")

def detail(request, id):
    return HttpResponse("sdsdsd")