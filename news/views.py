from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("<h1>News - Home</h1>")

def about(request):
    return HttpResponse("<h1>News - About</h1>")

def category(request):
    return HttpResponse("<h1>News - Category</h1>")







# news
    # - index
    # - about
    # - contact
    # - team
# events
    # - index
    # - about
    # - contact
    # - team
# category
    # - index
    # - about
    # - contact
    # - team