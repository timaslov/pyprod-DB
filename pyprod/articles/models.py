from django.shortcuts import reverse
from django.db import models
from django.conf import settings

from .const import ArticleStatus


class Article(models.Model):
    title = models.CharField(max_length=255)
    tagline = models.CharField(max_length=255, blank=True)
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL, related_name="children")
    content = models.TextField("content", blank=True)
    slug = models.SlugField("slug", max_length=64, unique=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, default=None, on_delete=models.SET_NULL)
    tags = models.ManyToManyField("Tag", blank=True)
    images = models.ManyToManyField("Image", blank=True)
    status = models.CharField(choices=ArticleStatus.choices, default=ArticleStatus.DRAFT, max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "article"
        verbose_name_plural = "articles"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article", kwargs={"slug": self.slug})


class Comment(models.Model):
    article = models.ForeignKey("Article", on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, related_name="comments", on_delete=models.CASCADE)
    text = models.CharField(max_length=2047)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        repr_len = len(str(self.author)) + len(str(self.text))
        return f"{self.author}: {self.text if repr_len < 70 else self.text[:70] + '...'}"


class Tag(models.Model):
    name = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url
