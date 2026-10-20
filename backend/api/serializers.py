"""Сериализаторы для API."""

from board.models import Note
from rest_framework.serializers import (
    ModelSerializer,
    PrimaryKeyRelatedField,
)


class BoardSerializer(ModelSerializer):
    """Сериализатор для сущности Board."""

    class Meta:
        model = Note
        fields = (
            'id',
            'title',
            'content',
            'owner',
            'created_at',
            'updated_at',
        )
        read_only_fields = (
            'owner',
            'created_at',
            'updated_at',
        )
