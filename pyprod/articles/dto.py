from datetime import datetime
from dataclasses import dataclass

from .const import ArticleStatus


@dataclass
class ArticleDTO:
    title: str
    tagline: str
    content: str
    slug: str
    status: ArticleStatus
    parent_id: int | None = None
    id: int | None = None
    author_id: int | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None


@dataclass
class CommentDTO:
    text: str
    article_id: int
    author_id: int
    id: int | None = None
    created_at: datetime | None = None
