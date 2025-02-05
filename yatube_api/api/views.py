from django.core.exceptions import PermissionDenied
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response

from posts.models import Comment, Group, Post

from .serializers import CommentSerializer, GroupSerializer, PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """Вьюсет управления комментариями."""

    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Фильтрация комментариев по post_id."""
        post_id = self.kwargs.get('post_id')
        if post_id:
            return Comment.objects.filter(post_id=post_id)
        return Comment.objects.all()

    def perform_create(self, serializer):
        """Создает объект автора и поста."""
        serializer.save(
            author=self.request.user,
            post=Post.objects.get(id=self.kwargs.get('post_id'))
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


class GroupViewSet(viewsets.ModelViewSet):
    """Вьюсет для получения информации по группам."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """Запрет создания групп через Api."""
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class PostViewSet(viewsets.ModelViewSet):
    """Вьюсет управления постами."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

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
