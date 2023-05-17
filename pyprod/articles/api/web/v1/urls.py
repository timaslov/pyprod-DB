from rest_framework import routers

from django.urls import path, include

from . import views

router = routers.SimpleRouter()
router.register("articles", views.ArticleViewSet, basename="article")
router.register("comments", views.CommentViewSet, basename="comment")


urlpatterns = [
    path("", include(router.urls)),
]
