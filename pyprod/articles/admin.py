from django.contrib import admin
from .models import Article


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
        "status",
        "created_at",
        "updated_at",
    ]
