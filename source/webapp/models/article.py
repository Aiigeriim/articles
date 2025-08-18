from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from webapp.models.base_create_update import BaseCreateUpdateModel

statuses = [("new", "Новая"), ("moderated", "Модерированная"), ("deleted", "Удаленные")]


class Article(BaseCreateUpdateModel):
    title = models.CharField(max_length=50, verbose_name='Название', null=False, blank=False)
    content = models.TextField(verbose_name='Контент')
    author = models.ForeignKey(get_user_model(), related_name='articles', on_delete=models.SET_DEFAULT, default=1, verbose_name="Автор")
    like_users = models.ManyToManyField(get_user_model(), related_name='like_article', verbose_name="Лайки")
    status = models.CharField(max_length=20, verbose_name="Статус", choices=statuses, default=statuses[0][0])
    tags = models.ManyToManyField(
        "webapp.Tag",
        verbose_name='Теги',
        related_name='articles',
        blank=True,
        through='webapp.ArticleTag',
        through_fields=("article", "tag"),
    )

    def __str__(self):
        return f"{self.id} - {self.title}"

    class Meta:
        db_table = 'articles'
        verbose_name = 'Статья'
        verbose_name_plural = "Статьи"
        permissions = [("change_article_status", "Can change article status")]


    def get_absolute_url(self):
        return reverse('webapp:article-detail', kwargs={'pk': self.pk})