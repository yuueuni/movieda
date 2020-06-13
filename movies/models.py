from django.db import models
from django.conf import settings
# from django.contrib.auth import get_user_model
User = settings.AUTH_USER_MODEL


# Create your models here.
class Genre(models.Model):
    genre_code = models.IntegerField()
    genre = models.CharField(max_length=40)


class Actor(models.Model):
    actor = models.CharField(max_length=100)


class Director(models.Model):
    director = models.CharField(max_length=100)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    summary = models.TextField()
    release_date = models.DateTimeField()
    running_time = models.IntegerField()
    poster = models.URLField(null=True, blank=True)
    genres = models.ManyToManyField(Genre, blank=True, related_name='movies')
    actors = models.ManyToManyField(Actor, blank=True, related_name='movies')
    directors = models.ManyToManyField(Director, blank=True, related_name='movies')

class Review(models.Model):
    rank = models.IntegerField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    movies = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')