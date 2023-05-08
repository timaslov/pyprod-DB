from django.urls import include, path


urlpatterns = [
    path("web/", include("api.web.urls", namespace="web")),
]
