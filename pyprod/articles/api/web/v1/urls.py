from rest_framework import routers

from django.urls import path, include

from . import views

router = routers.SimpleRouter()
router.register("articles", views.ArticleViewSet, basename="article")
router.register("comments", views.CommentViewSet, basename="comment")
router.register("tags", views.TagViewSet, basename="tag")
router.register("images", views.ImageViewSet, basename="image")


urlpatterns = [
    path("", include(router.urls)),
]
