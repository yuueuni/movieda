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
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def detail_article(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'PUT':
        serializer = ArticleSerializer(data=request.data, instance=article)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': 'success update!', 'data': serializer.data})
    elif request.method == 'DELETE':
        article.delete()
        return Response({'message': 'success delete!'})
    else:
        serializer = ArticleDetailSerializer(article)
        return Response(serializer.data)