from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class ArticleStatus(TextChoices):
    DRAFT = "draft", _("draft")
    PUBLISHED = "published", _("published")
    DELETED = "deleted", _("deleted")


ARTICLE_TREE_FIELDS = {
    "title",
    "tagline",
    "slug",
    "author",
    "updated_at",
}
