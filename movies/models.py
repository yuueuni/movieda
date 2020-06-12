from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Genre(models.Model):
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
    genres = models.ManyToManyField(Genre, related_name='movies')
    actors = models.ManyToManyField(Actor, related_name='movies')
    directors = models.ManyToManyField(Director, related_name='movies')


class Review(models.Model):
    rank = models.IntegerField()
    content = models.TextField()
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    movies = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')