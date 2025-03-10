# hexlet_django_blog/article/views.py
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views import View


class ArticleIndexView(View):

    def get(self, request, tags=None, article_id=None):

        if tags and article_id:
            context = {
                'title': 'ARTICLE',
                'tags': tags,
                'article_id': article_id
            }
            return render(request, 'articles/index.html', context)

        return redirect(
            reverse(
                'article_detail',
                kwargs={'tags': 'python',
                        'article_id': 42
                        }
                )
                )
