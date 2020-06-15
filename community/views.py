from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Article, Comment
from .serializers import ArticleSerializer, ArticleDetailSerializer, CommentSerializer


@api_view(['GET'])
def index(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_article(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(writer=request.user)
        return Response({'message': 'success save!', 'data': serializer.data})


@api_view(['GET', 'PUT', 'DELETE'])
def detail_article(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comments = article.comments.all()
    if request.user == article.writer:
        if request.method == 'PUT':
            serializer = ArticleSerializer(data=request.data, instance=article)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'message': 'success update!', 'article': serializer.data, 'comments': comments})
        elif request.method == 'DELETE':
            article.delete()
            return Response({'message': 'success delete!'})
    elif request.method == 'GET':
        serializer = ArticleDetailSerializer(article)
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_comment(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article, commenter=request.user)
    return Response({'message': 'success save comment!'})


@api_view(['PUT', 'DELETE'])
def detail_comment(request, article_pk, comment_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user == comment.commenter:
        if request.method == 'PUT':
            serializer = CommentSerializer(data=request.data, instance=comment)
            if serializer.is_valid(raise_exception=True):
                serializer.save(article=article, commenter=request.user)
                return Response({'message': 'success update comment!', 'data': serializer.data})
        elif request.method == 'DELETE':
            comment.delete()
            return Response({'message': 'success delete comment!'})