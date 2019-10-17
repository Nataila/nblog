#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: cc
# @Date  :2019-10-16


from django import template

import markdown

register = template.Library()


@register.filter
def md(content):
    res = markdown.markdown(
        content,
        extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ],
    )
    return res
