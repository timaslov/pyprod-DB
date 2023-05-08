from rest_framework import serializers

from .models import Article
from .const import ARTICLE_TREE_FIELDS


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            "title",
            "tagline",
            "content",
            "slug",
            "author",
            "status",
            "created_at",
            "updated_at",
        ]


class ArticleTreeSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = list(ARTICLE_TREE_FIELDS) + ["children"]

    @staticmethod
    def get_children(obj):
        child_articles = obj.children.only(*ARTICLE_TREE_FIELDS)
        return ArticleTreeSerializer(child_articles, many=True).data
