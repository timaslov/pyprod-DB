from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from ....permissions import IsStaffOrReadOnly, IsSuperUserOrReadOnly
from ....dal import get_core_subjects
from ....const import ArticleStatus
from ....models import Article, Comment, Tag, Image
from ....serializers import (
    ArticleTreeSerializer,
    ArticleSerializer,
    CommentSerializer,
    TagSerializer,
    ImageSerializer,
)
import logging
import time


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all().order_by("-created_at")
    serializer_class = ArticleSerializer
    lookup_field = "slug"
    permission_classes = [IsStaffOrReadOnly]
    filterset_fields = ("author", "status")

    def perform_create(self, serializer):
        status = ArticleStatus.PUBLISHED if self.request.user.is_superuser else ArticleStatus.DRAFT
        serializer.save(author=self.request.user, status=status)

    def perform_update(self, serializer):
        status = ArticleStatus.PUBLISHED if self.request.user.is_superuser else ArticleStatus.DRAFT
        serializer.save(author=self.request.user, status=status)

    @action(detail=False)
    def index(self, request):
        core_subjects = get_core_subjects()
        result = []
        for core_subject in core_subjects:
            result.append(ArticleTreeSerializer(core_subject).data)

        return Response(result)


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all().order_by("-created_on")
    serializer_class = CommentSerializer
    filterset_fields = ("article_id", )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all().order_by("-created_on")
    serializer_class = TagSerializer
    permission_classes = [IsSuperUserOrReadOnly]


class ImageViewSet(ModelViewSet):
    queryset = Image.objects.all().order_by("-created_on")
    serializer_class = ImageSerializer
    permission_classes = [IsSuperUserOrReadOnly]
