# hexlet_django_blog/article/views.py
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'articles/index.html', context={
        'title': 'ARTICLE',
    })
