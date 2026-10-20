"""Viewsets для API."""

from board.models import Note
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from .serializers import BoardSerializer


class BoardViewSet(viewsets.ModelViewSet):
    """ViewSet для сущности Board."""

    queryset = Note.objects.all()
    serializer_class = BoardSerializer
    permission_classes = (IsAuthenticated,)

    # def get_queryset(self):
    #     return Note.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
