from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from .serializers import CommentSerializer, GroupSerializer, PostSerializer
from posts.models import Group, Post


class CommentViewSet(viewsets.ModelViewSet):
    """Вьюсет управления комментариями."""

    serializer_class = CommentSerializer

    def get_post(self):
        """Получение поста."""
        return get_object_or_404(Post, id=self.kwargs.get('post_id'))

    def get_queryset(self):
        """Фильтрация комментариев по post_id."""
        post = self.get_post()
        return post.comments.all()

    def perform_create(self, serializer):
        """Создает объект автора и поста."""
        serializer.save(
            author=self.request.user,
            post=self.get_post()
        )

    def perform_update(self, serializer):
        """Проверка прав на изменение контента."""
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        super(CommentViewSet, self).perform_update(serializer)

    def perform_destroy(self, instance):
        """Проверка прав на удаление контента."""
        if instance.author != self.request.user:
            raise PermissionDenied('Удаление чужого контента запрещено!')
        return super().perform_destroy(instance)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    """Вьюсет управления постами."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        """Создает объект автора."""
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        """Проверка прав на изменение контента."""
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        super(PostViewSet, self).perform_update(serializer)

    def perform_destroy(self, instance):
        """Проверка прав на удаление контента."""
        if instance.author != self.request.user:
            raise PermissionDenied('Удаление чужого контента запрещено!')
        return super().perform_destroy(instance)
