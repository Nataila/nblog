#!/usr/bin/env python
# coding: utf-8
# cc @ 2017-09-28

from __future__ import unicode_literals

from django.views.generic import ListView
from models import Posts


class HomeView(ListView):
    """
    首页
    """
    template_name = 'nblog/home.html'
    model = Posts
