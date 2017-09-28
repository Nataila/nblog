#!/usr/bin/env python
# coding: utf-8
# cc @ 2017-09-27

from django.contrib import admin

from .models import Tags, Posts


class TagsAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')


class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')

    def get_media(self):
        js = (
            '/static/plugins/ueditor/ueditor.config.js',
            '/static/plugins/ueditor/ueditor.all.js',
            '/static/plugins/ueditor/config.js',
        )
        css = [
            '/static/css/admin.css',
        ]
        media = super(PostsAdmin, self).get_media()
        media.add_js(js)
        media.add_css({'screen': css})
        return media


admin.site.register(Tags, TagsAdmin)
admin.site.register(Posts, PostsAdmin)
