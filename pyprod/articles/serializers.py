from rest_framework import serializers

from .models import Article, Comment, Tag, Image
from .const import ARTICLE_TREE_FIELDS


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            "id",
            "name",
            "created_on",
        ]


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = [
            "id",
            "name",
            "url",
            "created_on",
        ]


class ArticleSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False)
    images = ImageSerializer(many=True, required=False)

    class Meta:
        model = Article
        fields = [
            "id",
            "title",
            "tagline",
            "content",
            "slug",
            "author",
            "tags",
            "images",
            "parent",
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


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            "id",
            "article",
            "author",
            "text",
            "created_on",
        ]
