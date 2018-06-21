#!/usr/bin/env python
# coding: utf-8
# cc @ 2017-09-27

from django.contrib import admin

from .models import Tags, Posts


class TagsAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')


class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')


admin.site.register(Tags, TagsAdmin)
admin.site.register(Posts, PostsAdmin)
