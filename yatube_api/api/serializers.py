from rest_framework import serializers

from posts.models import Comment, Group, Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True, )
    post = serializers.PrimaryKeyRelatedField(read_only=True, )

    class Meta:
        model = Comment
        fields = ('author', 'post', 'text', 'created')


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('title', 'slug', 'description')


class PostSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True, )
    pub_date = serializers.DateTimeField(read_only=True, )

    class Meta:
        model = Post
        fields = ('id', 'text', 'pub_date', 'author', 'image', 'group')
