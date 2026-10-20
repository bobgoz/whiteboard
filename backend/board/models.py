"""Модели приложения Board."""

from django.contrib.auth import get_user_model
from django.db import models
from django.conf import settings

from .constants import (
    DESCRIPTION_MAX_LENGTH,
    TITLE_MAX_LENGTH,
)


class Note(models.Model):
    """Доска для организации заметок."""

    title = models.CharField(
        'Название',
        max_length=TITLE_MAX_LENGTH,
    )
    content = models.CharField(
        'Содержимое заметки',
        max_length=DESCRIPTION_MAX_LENGTH,
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='notes',
        verbose_name='Владелец',
    )
    created_at = models.DateTimeField(
        'Дата создания',
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        'Дата обновления',
        auto_now=True,
    )

    class Meta:
        verbose_name = 'доска'
        verbose_name_plural = 'доски'
        ordering = ('-updated_at',)

    def __str__(self):
        return f'{self.title} - {self.owner}'  # TODO
