# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from .models import Post, Category, Tag



def index(request):
    #return HttpResponse('<h1>Hello World!!!</h1>')
    tags2 = Tag.objects.all()
    category = Category.objects.all()
    posts = Post.objects.all().order_by('-created_at')[:10]

    query = request.GET.get("q") 
    if query:
       posts = Post.objects.filter(title__contains=query)

    

    context = {
        'posts': posts,
        'tags2': tags2,
        'category': category,     
    }

    return render(request, 'index.html', context, query)


# def details(request,id):
def details(request,slug):
    #post = Post.objects.get(id=id)  
    tags2 = Tag.objects.all()  
    category = Category.objects.all()

    post = Post.objects.get(slug=slug)
    
    context = {
        'post': post,
        'tags2': tags2,
        'category': category, 
    }
    return render(request, 'details.html', context)

def category(request,id):
    tags2 = Tag.objects.all()
    category = Category.objects.all()
    posts = Post.objects.filter(category=id)

    context = {
        'posts': posts,
        'tags2': tags2,
        'category': category, 
    }
    return render(request, 'category.html', context)


def tag(request,slug,id):     
    tags2 = Tag.objects.all()
    category = Category.objects.all()  
    tags = Tag.objects.get(slug=slug)
    posts = Post.objects.filter(tags=id)
    
    context = {
        'tags': tags,
        'posts': posts,
        'tags2': tags2,
        'category': category, 
    }
    return render(request, 'tag.html', context)

