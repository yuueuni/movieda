from rest_framework import serializers
from .models import Article, Comment

from accounts.serializers import UserSerializer


class ArticleSerializer(serializers.ModelSerializer):
    writer = UserSerializer(required=False)

    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'writer', 'created_at', 'updated_at',)
        read_only_fields = ('id', 'writer', 'created_at', 'updated_at',)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'content',)


class ArticleDetailSerializer(serializers.ModelSerializer):
    writer = UserSerializer()
    comments = CommentSerializer(many=True)

    class Meta:
        model = Article
        fields = ArticleSerializer.Meta.fields + ('comments',)
