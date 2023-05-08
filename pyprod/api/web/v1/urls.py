from django.urls import path, include


app_name = "v1"

urlpatterns = [
    path("articles/", include("articles.api.web.v1.urls")),
    path("users/", include("core.users.api.web.v1.urls")),
]
