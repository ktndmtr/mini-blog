from django.contrib import admin
from django.utils.html import format_html_join, mark_safe

from .models import Blog, Blogger, Comment


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ('comments',)
    fields = ('name', 'author', 'content', 'comments')

    @admin.display(description='Comments')
    def comments(self, instance):
        return format_html_join(
            mark_safe('<hr>'),
            '<p>{}<p>',
            ((comment, ) for comment in instance.comment_set.all()),
        )


@admin.register(Blogger)
class BloggerAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fields = ('blog', 'author', 'content')
    list_display = ('blog', 'author', 'post_date', 'truncated_content')

    @admin.display(description='Content')
    def truncated_content(self, instance):
        return instance.content[:75]
