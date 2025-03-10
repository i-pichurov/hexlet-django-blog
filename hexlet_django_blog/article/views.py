# hexlet_django_blog/article/views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class ArticleIndexView(View):

    def get(self, request, *args, **kwargs):
        context = {'title': 'ARTICLE'}
        return render(request, 'articles/index.html', context)
