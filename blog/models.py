# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.db import models

from django.contrib.auth.models import User

from django.template.defaultfilters import slugify

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):    
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Tag, self).save(*args,**kwargs)

    

class Post(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    body = models.TextField()
    description = models.CharField(max_length=250)
    created_at = models.DateTimeField(default=datetime.now(), blank=True)
    state = models.BooleanField(default=True)
    picture = models.FileField(blank=True)
    slug = models.SlugField(blank=True)
    
    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Post, self).save(*args,**kwargs)

