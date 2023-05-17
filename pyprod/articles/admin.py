from django.contrib import admin
from .models import Article, Comment


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
        "status",
        "created_at",
        "updated_at",
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ("article", "author", "text", "created_on")
    list_display = ("id", "article", "author", "text", "created_on") # видимость полей в админке
    readonly_fields = [
        "created_on",
    ]
    fields = [
        "article",
        "author",
        "text",
        "created_on"
    ]
