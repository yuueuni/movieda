from rest_framework import serializers
from .models import Article, Comment

from accounts.serializers import UserSerializer


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'content',)


class ArticleDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    comments = CommentSerializer(many=True)

    class Meta:
        model = Article
        fields = ArticleSerializer.Meta.Fields + ('comments',)
