#!/usr/bin/env python
# coding: utf-8
# cc @ 2017-09-28

from __future__ import unicode_literals

from django.views.generic import ListView, DetailView

from .models import Posts, Tags


class HomeView(ListView):
    """
    首页
    """
    template_name = 'nblog/home.html'
    model = Posts
    paginate_by = 10

    def get_queryset(self, *args, **kwargs):
        tag = self.request.GET.get('tag')
        if tag:
            return Posts.objects.filter(tags=tag)
        return Posts.objects.all()

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['tag_list'] = Tags.objects.all()
        tag = self.request.GET.get('tag')
        if tag:
            context['tag'] = tag
        return context


class PostDetailView(DetailView):
    """
    文章详情
    """
    template_name = 'nblog/post.html'
    model = Posts
    context_object_name = 'post_detail'
    queryset = Posts.objects.all()
