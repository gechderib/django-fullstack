from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by("date")
    return render(request, "articles/article_list.html",{"articles":articles})

def article_detail(request, slug):
    # return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request, "articles/article_detail.html",{"article":article})


@login_required()
def article_create(request):
    form = forms.CreateArticle()
    print(form)
    return render(request, "articles/article_create.html",{"form":form})