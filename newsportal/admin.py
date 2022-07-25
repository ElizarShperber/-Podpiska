from django.contrib import admin

from newsportal.models import Author, Category, Post, PostCategory, Comment, Subscriber

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Comment)
admin.site.register(Subscriber)