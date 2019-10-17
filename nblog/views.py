#!/usr/bin/env python
# coding: utf-8
# cc @ 2017-09-28

from __future__ import unicode_literals

from django.views.generic import ListView, DetailView
from django.db.models import Q

from .models import Posts


class HomeView(ListView):
    """
    首页
    """

    template_name = 'nblog/home.html'
    model = Posts
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        tag = self.request.GET.get('tag')
        search = self.request.GET.get('search')
        if tag:
            return Posts.objects.filter(tags=tag)
        if search:
            return Posts.objects.filter(
                Q(title__contains=search) | Q(content__contains=search)
            )
        return Posts.objects.all()

    # def get_context_data(self, **kwargs):
    #     context = super(HomeView, self).get_context_data(**kwargs)
    #     context['tag_list'] = Tags.objects.all()
    #     tag = self.request.GET.get('tag')
    #     if tag:
    #         context['tag'] = tag
    #     return context


class PostDetailView(DetailView):
    """
    文章详情
    """

    template_name = 'nblog/post.html'
    model = Posts
    context_object_name = 'post_detail'
    queryset = Posts.objects.all()
