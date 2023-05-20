from django.contrib import admin
from .models import Article, Comment, Tag, Image


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    search_fields = ("title", "tagline", "content")
    list_display = ("title", "slug", "updated_at", "status")
    readonly_fields = [
        "created_at",
        "updated_at",
    ]
    fields = [
        "title",
        "tagline",
        "parent",
        "content",
        "slug",
        "author",
        "tags",
        "images",
        "status",
        "created_at",
        "updated_at",
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ("article", "author", "text")
    list_display = ("id", "article", "author", "text", "created_on")
    readonly_fields = [
        "created_on",
    ]
    fields = [
        "article",
        "author",
        "text",
        "created_on"
    ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("id", "name", "created_on")
    readonly_fields = [
        "created_on",
    ]
    fields = [
        "name",
        "created_on"
    ]


@admin.register(Image)
class TagAdmin(admin.ModelAdmin):
    search_fields = ("name", "url")
    list_display = ("id", "name", "url", "created_on")
    readonly_fields = [
        "created_on",
    ]
    fields = [
        "name",
        "url",
        "created_on"
    ]
