#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: cc
# @Date  :2019-01-09

from django.conf import settings


def constants_context_processor(request):
    '''
    模版里的全局变量
    '''
    ctx = {
        'settings': settings,
    }
    return ctx
