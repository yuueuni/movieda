from django.db import models
from django.contrib.auth import get_user_model
from movies.models import Movie
User = get_user_model()

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    movies = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')

    @property
    def formatted_created_at(self):
        return self.created_at.strftime('%Y-%m-%d %H:%M')

    @property
    def formatted_updated_at(self):
        return self.updated_at.strftime('%Y-%m-%d %H:%M')

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')

    @property
    def formatted_created_at(self):
        return self.created_at.strftime('%Y-%m-%d %H:%M')

    @property
    def formatted_updated_at(self):
        return self.updated_at.strftime('%Y-%m-%d %H:%M')
