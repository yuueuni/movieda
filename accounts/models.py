from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from movies.models import Actor, Director, Movie

# Create your models here.
class User(AbstractUser):
    birthday = models.DateTimeField(null=True)
    gender = models.BooleanField(default=True)
    favorite_actors = models.ManyToManyField(Actor, blank=True, related_name='users')
    favorite_directors = models.ManyToManyField(Director, blank=True, related_name='users')
    favorite_movies = models.ManyToManyField(Movie, blank=True, related_name='users')


# 생각해보니까 없어도 될거같음.

# from movies.models import Genre
# class Favor(models.Model):
#     favor_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favors')
#     genre_name = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='favors')
#     cnt = models.IntegerField()