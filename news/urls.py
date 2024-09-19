from django.urls import path

from .views import *

urlpatterns = [
    
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('news_detail/<int:id>', detail, name='news_detail'),
    path('category/<int:id>', show_category, name='category'),
]
