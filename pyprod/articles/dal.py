from django.db.models import QuerySet
from .models import Article


def get_core_subjects() -> QuerySet:
    return Article.objects.filter(parent__isnull=True)
