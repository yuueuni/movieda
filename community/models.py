from django.db import models
from django.contrib.auth import get_user_model
from movies.models import Movie
from datetime import datetime

User = get_user_model()
now = datetime.now()
# now.strftime('%Y-%m-%d %H:%M')

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    movies = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.CharField(default=now.strftime('%Y-%m-%d %H:%M'), max_length=100)
    updated_at = models.DateTimeField(auto_now=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')