#!/usr/bin/env python
# coding: utf-8
# cc @ 2017-09-27

from django.db import models
from mdeditor.fields import MDTextField


class Tags(models.Model):
    """
    标签
    """

    name = models.CharField(max_length=200, verbose_name=u"标签名称")
    created_at = models.DateTimeField(
        verbose_name=u'创建时间', editable=False, auto_now_add=True
    )

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = u"标签"


def m2mdefault():
    try:
        return [Tags.objects.first().pk]
    except:
        return []


class Posts(models.Model):
    """
    文章
    """

    TYPE_CHOICES = [(1, u'原创'), (2, u'转载')]

    title = models.CharField(max_length=200, verbose_name=u"文章标题")
    content = MDTextField(verbose_name='内容')
    link = models.CharField(max_length=200, verbose_name=u"原文地址", blank=True)
    tags = models.ManyToManyField(Tags, default=m2mdefault)
    blog_type = models.IntegerField(choices=TYPE_CHOICES, default=1)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')

    class Meta:
        ordering = ['-created_at']
        verbose_name = verbose_name_plural = u"文章"
