from django.views.generic import RedirectView
from django.urls import path, include


urlpatterns = [
    path("", RedirectView.as_view(pattern_name="core_subjects")),
    path("api/", include("api.urls")),
]
